from celery import shared_task
from .models import Tool, News
from django.utils import timezone

"""Celery tasks for catalog domain.

Tasks included:
 - refresh_tool_stats(tool_id): placeholder to recompute metrics for one tool.
 - fetch_news_for_tool(tool_id): placeholder that simulates fetching external news.
 - refresh_all_featured_tools(): iterates through featured tools and triggers per-tool refresh.
 - fetch_recent_news_for_featured_tools(): iterates through featured tools and enqueues news fetch.

In producción estas tareas se reemplazarán con lógica real (requests a APIs, scraping
controlado vía n8n, análisis de métricas, embeddings, etc.). Mantenerlas ligeras garantiza
que el pipeline asíncrono sea verificable desde el inicio del MVP.
"""


@shared_task
def refresh_tool_stats(tool_id: int):
    # Placeholder: compute rating or metrics aggregation
    tool = Tool.objects.filter(id=tool_id).first()
    if tool:
        # In a real scenario aggregate related usage metrics
        tool.updated_at = timezone.now()
        tool.save(update_fields=['updated_at'])
    return True


@shared_task
def fetch_news_for_tool(tool_id: int):
    # Placeholder for external fetch logic
    tool = Tool.objects.filter(id=tool_id).first()
    if not tool:
        return False
    # Example: create a dummy news entry (would be replaced by real fetch)
    News.objects.get_or_create(
        url=f'https://example.com/news/{tool.slug}-{timezone.now().timestamp()}',
        defaults={
            'tool': tool,
            'title': f'Update for {tool.name}',
            'published_at': timezone.now(),
            'summary': 'Auto-generated placeholder.'
        }
    )
    return True


@shared_task
def refresh_all_featured_tools():
    """Refresca stats de todas las herramientas destacadas.

    Usa refresh_tool_stats.delay para desacoplar y permitir reintentos individuales.
    """
    for tool_id in Tool.objects.filter(is_featured=True).values_list('id', flat=True):
        refresh_tool_stats.delay(tool_id)
    return True


@shared_task
def fetch_recent_news_for_featured_tools():
    """Encola tareas de fetch de noticias para herramientas destacadas.

    Futuro: deduplicar, controlar ventana de tiempo y limitar concurrencia.
    """
    for tool_id in Tool.objects.filter(is_featured=True).values_list('id', flat=True):
        fetch_news_for_tool.delay(tool_id)
    return True
