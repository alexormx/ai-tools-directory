# 🤖 Instrucciones para Agentes – AI Tools Directory

Guía concisa para un agente actuando como Senior Full Stack (Django REST + React/Vite + Docker + Celery + n8n). Foco: entregar cambios accionables y verificables.

## 1. Rol & Formato de Respuesta
Siempre incluye: 1) Resumen acción, 2) Comandos (bash), 3) Diffs o archivos completos nuevos, 4) Cómo probar (curl/URLs), 5) Criterios de aceptación, 6) Próximos pasos si aplica. Usa Conventional Commits en ejemplos.

## 2. Arquitectura Snapshot (estado actual MVP)
Servicios en `docker-compose.yml`: frontend (Next.js + Chakra, puerto 3000, SSG/ISR), backend (placeholder Django puerto 8000), db (Postgres 15), redis, celery, celery_beat, n8n (5678). Backend aún no implementado. Directorios planeados: `ai_pipelines/`, `automations/`.

## 3. Variables de Entorno Clave (usar `.env` / `.env.example`)
DJANGO_SECRET_KEY, DJANGO_DEBUG, ALLOWED_HOSTS, DATABASE_URL, REDIS_URL, CELERY_BROKER_URL, CELERY_RESULT_BACKEND, CORS_ALLOWED_ORIGINS, N8N_WEBHOOK_SECRET. Nunca hardcodear secretos en commits.

## 4. Convenciones & Branching
Rama principal: `main`. Branches: `feat/<area>-<slug>`, `fix/...`, `chore/...`. Commits: `feat:`, `fix:`, `docs:` etc. Código en inglés; documentación en español. No introducir frameworks fuera del stack sin justificación.

## 5. Prioridades Iniciales (cuando se solicite implementar backend)
1. Completar `backend/requirements.txt` (versiones fijadas: Django, djangorestframework, gunicorn, psycopg2-binary, celery, redis, django-cors-headers, djangorestframework-simplejwt, django-filter, pytest, pytest-django).
2. Scaffold Django: `manage.py`, paquete `config/` (settings, urls, wsgi, asgi opcional, celery). Activar: DRF, corsheaders, rest_framework_simplejwt, django_filters.
3. App `catalog`: modelos Category, Tag, Tool (M2M Category + M2M Tag), Source, News. Slugs únicos, timestamps auto.
4. Serializers + ViewSets + Router `/api/` con filtros (django-filter), búsqueda (`?search=` en name, tags), paginación 20, orden por `-created_at`.
5. Endpoint ingest seguro: `POST /api/news/ingest/` validando header `X-Webhook-Secret` contra `N8N_WEBHOOK_SECRET`.
6. Celery: tareas `refresh_tool_stats`, `fetch_news_for_tool`, Beat job periódico (ej: cada 6h featured tools news).
7. Tests pytest: models, una view list, ingest (401 sin header, 200 con header), una tarea Celery (utilizar `CELERY_TASK_ALWAYS_EAGER` en settings test).

## 6. Frontend (Next.js + Chakra)
Estructura App Router (`frontend/app/*`). Páginas: `/` (home), `/tools`, `/tools/[slug]`, `/news`. Revalidación ISR: tools 1h, news 15m. Cliente fetch nativo (`fetch` + rutas en `lib/api.ts`). Añadir JSON-LD y meta tags cuando el backend provea datos reales. Para nuevas páginas usar SSG con `export const revalidate`.

## 7. Flujo de Trabajo Común
Levantar stack: `docker compose up --build`. Logs backend: `docker compose logs -f backend`. Ejecutar migraciones tras scaffold: `docker compose exec backend python manage.py migrate`. Tests: `docker compose exec backend python -m pytest -q`. Crear superusuario: `docker compose exec backend python manage.py createsuperuser`.

## 8. Patrones Técnicos Backend (esperados al crear código)
Settings: leer DATABASE_URL/REDIS_URL; CORS_ALLOWED_ORIGINS; REST_FRAMEWORK (DefaultPagination=20, filters, SearchFilter, OrderingFilter). Autenticación admin: SimpleJWT (solo métodos de escritura). Público: GET a tools/categories/news.

## 9. n8n / Ingesta Noticias
Workflow enviará POST firmado a `/api/news/ingest/` con campos normalizados (title, url, published_at, source.kind, tool_slug opcional). Evitar duplicados por hash de url. Responder 201 o 200 idempotente.

## 10. Criterios de Aceptación Globales (MVP backend+frontend)
1) Contenedores suben sin errores. 2) Endpoints listan datos con paginación y filtros. 3) Celery ejecuta tarea y Beat agenda una periódica. 4) Frontend consume `/api/tools/` y abre detalle. 5) Ingest valida secreto. 6) Tests ≥80% cobertura base (al menos modelos + vistas clave).

## 11. Errores a Evitar
No olvidar reconstruir imagen tras editar `requirements.txt`. No exponer SECRET_KEY. No mezclar puertos (mantener 3000 FE, 8000 API). No introducir dependencias pesadas de IA antes de aislarlas en `ai_pipelines/`.

## 12. Estilo de Diffs / Ejemplo Comando
Incluir fragmentos cambiados claramente:
```
# docker-compose.yml (fragmento)
 services:
   backend:
     command: bash -lc "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
```

## 13. Próximos Pasos Potenciales
Scaffold backend Django + API real, añadir tests Pytest, incorporar React Query solo si el caching de fetch nativo no basta, implementar JSON-LD, sitemap y robots.txt, añadir Makefile, `render.yaml` y CI.

---
Solicita más detalle si necesitas plantillas concretas (ej: `settings.py`, modelos o tareas Celery) y genera diffs completos al implementarlos.
