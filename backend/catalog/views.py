from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils import timezone
from django.db import IntegrityError
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError
import redis as redis_lib
from celery import current_app as celery_app

from .models import Category, Tag, Tool, Source, News
from .serializers import CategorySerializer, TagSerializer, ToolSerializer, SourceSerializer, NewsSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    search_fields = ['name']


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer
    search_fields = ['name']


class ToolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tool.objects.all().order_by('-created_at')
    serializer_class = ToolSerializer
    filterset_fields = ['pricing', 'is_featured', 'categories__slug', 'tags__slug']
    search_fields = ['name', 'description', 'tags__name']
    ordering_fields = ['created_at', 'name']


class SourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Source.objects.all().order_by('name')
    serializer_class = SourceSerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.select_related('tool', 'source').order_by('-published_at', '-created_at')
    serializer_class = NewsSerializer
    filterset_fields = ['tool__slug', 'source__kind']
    search_fields = ['title', 'tool__name']
    ordering_fields = ['published_at', 'created_at']


@api_view(['POST'])
@permission_classes([AllowAny])
def ingest_news(request):
    secret = request.headers.get('X-Webhook-Secret')
    if not settings.N8N_WEBHOOK_SECRET or secret != settings.N8N_WEBHOOK_SECRET:
        return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    payload = request.data
    url = payload.get('url')
    if not url:
        return Response({'detail': 'Missing url'}, status=status.HTTP_400_BAD_REQUEST)

    # Optional tool mapping
    tool_slug = payload.get('tool_slug')
    tool = None
    if tool_slug:
        tool = Tool.objects.filter(slug=tool_slug).first()

    source_kind = payload.get('source', {}).get('kind', 'rss')
    source_name = payload.get('source', {}).get('name', source_kind.upper())
    source_url = payload.get('source', {}).get('url', '')
    source, _ = Source.objects.get_or_create(name=source_name, defaults={'url': source_url or 'https://example.com', 'kind': source_kind})

    news_defaults = {
        'tool': tool,
        'title': payload.get('title', 'Sin título'),
        'published_at': payload.get('published_at') or timezone.now(),
        'source': source,
        'summary': payload.get('summary', '')
    }
    try:
        obj, created = News.objects.get_or_create(url=url, defaults=news_defaults)
    except IntegrityError:
        return Response({'detail': 'Conflict'}, status=status.HTTP_409_CONFLICT)

    serializer = NewsSerializer(obj)
    return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def health(_request):
    # DB check
    db_ok = True
    try:
        conn = connections['default']
        conn.cursor()
    except OperationalError:
        db_ok = False

    # Redis check (best-effort, no exception propagation)
    redis_ok = True
    try:
        redis_url = settings.CELERY_BROKER_URL
        r = redis_lib.from_url(redis_url, socket_connect_timeout=1, socket_timeout=1)
        r.ping()
    except Exception:  # pragma: no cover - degradación
        redis_ok = False

    # Celery availability: check that at least one task registry exists (core tasks always loaded)
    celery_ok = True
    try:
        # Using built-in ping via app.control.inspect would require a running worker; here just ensure loader ran
        celery_ok = bool(celery_app.tasks) and 'celery.backend_cleanup' in celery_app.tasks
    except Exception:  # pragma: no cover
        celery_ok = False

    overall = db_ok and redis_ok and celery_ok
    status_code = 200 if overall else 503
    return Response({
        'status': 'ok' if overall else 'degraded',
        'components': {
            'db': db_ok,
            'redis': redis_ok,
            'celery': celery_ok,
        }
    }, status=status_code)
