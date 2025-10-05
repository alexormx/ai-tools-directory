from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from catalog.views import CategoryViewSet, TagViewSet, ToolViewSet, NewsViewSet, SourceViewSet, ingest_news, health

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('tags', TagViewSet)
router.register('tools', ToolViewSet)
router.register('sources', SourceViewSet)
router.register('news', NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Colocar ingest antes de incluir router, o usar un slug distinto
    path('api/news/ingest/', ingest_news, name='news-ingest'),
    path('api/', include(router.urls)),
    path('health/', health, name='health'),
]
