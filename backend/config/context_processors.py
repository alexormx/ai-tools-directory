from catalog.models import Tool, Category, Tag, News

def dashboard_metrics(request):  # pragma: no cover (ligero y simple)
    try:
        return {
            'metric_tool_count': Tool.objects.count(),
            'metric_category_count': Category.objects.count(),
            'metric_tag_count': Tag.objects.count(),
            'metric_news_count': News.objects.count(),
        }
    except Exception:
        # Evita fallo de admin si la migración aún no corrió
        return {
            'metric_tool_count': 0,
            'metric_category_count': 0,
            'metric_tag_count': 0,
            'metric_news_count': 0,
        }
