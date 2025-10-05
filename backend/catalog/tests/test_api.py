import pytest
from django.urls import reverse
from catalog.models import Category, Tool


@pytest.mark.django_db
def test_health(client):
    r = client.get('/health/')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'


@pytest.mark.django_db
def test_tools_list_empty(client):
    r = client.get('/api/tools/')
    assert r.status_code == 200
    assert r.json()['count'] == 0


@pytest.mark.django_db
def test_tools_list_with_one(client):
    c = Category.objects.create(name='NLP')
    t = Tool.objects.create(name='Vectorizer')
    t.categories.add(c)
    r = client.get('/api/tools/?search=Vector')
    assert r.status_code == 200
    body = r.json()
    assert body['count'] == 1
    assert body['results'][0]['name'] == 'Vectorizer'


@pytest.mark.django_db
def test_ingest_requires_secret(client):
    # Enviar JSON explícito para evitar 415/405 confusiones
    r = client.post('/api/news/ingest/', data={'url': 'https://example.com/a'}, content_type='application/json')
    assert r.status_code == 401, r.content


@pytest.mark.django_db
def test_ingest_with_secret(settings, client):
    settings.N8N_WEBHOOK_SECRET = 'secret'
    r = client.post('/api/news/ingest/', data={'url': 'https://example.com/a', 'title': 'A'}, content_type='application/json', HTTP_X_WEBHOOK_SECRET='secret')
    assert r.status_code in (200, 201)
    data = r.json()
    assert data['url'] == 'https://example.com/a'


@pytest.mark.django_db
def test_celery_tasks_eager(settings):
    settings.CELERY_TASK_ALWAYS_EAGER = True
    from catalog.models import Tool
    from catalog.tasks import refresh_tool_stats, fetch_news_for_tool, refresh_all_featured_tools, fetch_recent_news_for_featured_tools
    tool = Tool.objects.create(name='Featured Tool', is_featured=True)
    assert refresh_tool_stats.delay(tool.id).get(timeout=5) is True
    assert fetch_news_for_tool.delay(tool.id).get(timeout=5) is True
    # Aggregated tasks should iterate without error
    assert refresh_all_featured_tools.delay().get(timeout=5) is True
    assert fetch_recent_news_for_featured_tools.delay().get(timeout=5) is True
