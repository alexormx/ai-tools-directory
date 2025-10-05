# 🧠 AI TOOLS DIRECTORY  
**Plataforma Inteligente de Herramientas y Tendencias en Inteligencia Artificial**  
Equipo de Desarrollo - IA Maverick – Octubre 2025  

---

## 🎯 Propósito del Proyecto
El proyecto **AI Tools Directory** tiene como propósito desarrollar una **plataforma web inteligente y automatizada** que centralice las **herramientas, recursos y tendencias más relevantes en el campo de la Inteligencia Artificial (IA)**.  

La iniciativa busca **simplificar el descubrimiento, análisis y selección de herramientas de IA**, integrando automatización, procesamiento de datos y modelos de aprendizaje automático para ofrecer una experiencia personalizada y en constante actualización.

---

## 🧩 Descripción General
**AI Tools Directory** funcionará como un **ecosistema informativo y colaborativo**, donde los usuarios podrán:  
- Consultar un **directorio centralizado de herramientas de IA**, clasificadas por categorías, objetivos y casos de uso.  
- Acceder a un **feed automatizado de noticias y artículos** actualizados de fuentes confiables.  
- Recibir **recomendaciones inteligentes** según sus intereses y actividad.  
- Participar en una **comunidad interactiva** con valoraciones y comentarios.  
- Configurar **alertas y resúmenes semanales** con tendencias y novedades relevantes.

El proyecto combina tecnologías modernas de backend, frontend y procesamiento de datos para lograr una plataforma escalable, automatizada y con alto valor educativo y profesional.

---

## ⚙️ Principales Funcionalidades

| Categoría | Descripción |
|------------|--------------|
| 🔍 **Directorio IA** | Base de datos actualizada con herramientas clasificadas por tipo, tecnología y aplicación. |
| 📰 **Noticias IA** | Ingesta automatizada de noticias desde RSS/APIs, con resumen generado por IA. |
| 🤖 **Recomendaciones** | Sugerencias basadas en similitud semántica y comportamiento del usuario. |
| 💬 **Comunidad** | Calificaciones, reseñas y sistema de reputación colaborativo. |
| 📡 **Alertas & Digest** | Envío automático de novedades y resumen semanal personalizado. |

---

## 🧠 Procesamiento Inteligente de Datos
El sistema integrará **pipelines de Inteligencia Artificial** que permitirán:

- Clasificación automática de herramientas mediante **NLP y embeddings** (OpenAI o HuggingFace).  
- Búsqueda semántica en el directorio mediante **similaridad vectorial** (FAISS o Qdrant).  
- Resumen automático de artículos con **modelos T5 o GPT-4o-mini**.  
- Etiquetado y categorización dinámica usando **Zero-Shot Classification** (`facebook/bart-large-mnli`).  
- Recomendaciones híbridas (content-based + collaborative filtering).

---

## 🧰 Stack Tecnológico

| Componente | Tecnologías | Rol |
|-------------|--------------|-----|
| **Frontend** | Next.js (App Router) + React 18 + Chakra UI | SSG/ISR para SEO y UI consistente |
| **Backend** | Python 3.11 + Django REST Framework | API modular, segura y escalable |
| **Automatización** | n8n (Docker) | Ingesta de datos y flujos ETL automatizados |
| **Procesamiento Asíncrono** | Celery + Redis | Ejecución programada de tareas |
| **Base de Datos** | PostgreSQL + FAISS / Qdrant | Datos estructurados y búsqueda semántica |
| **IA / NLP** | OpenAI API + HuggingFace Transformers | Clasificación, embeddings y resúmenes |
| **Infraestructura** | Docker + GitHub Actions + Render/Heroku | CI/CD y despliegue automatizado |
| **Autenticación** | JWT + Social Auth | Seguridad y facilidad de acceso |
| **Observabilidad** | Sentry / Prometheus | Monitoreo, métricas y trazabilidad |

---

## 🛠️ Tecnologías y Justificación Detallada

Esta sección documenta cada herramienta/lenguaje seleccionado (o planificado) y el porqué de su inclusión en el proyecto.

| Tecnología / Herramienta | Rol en el Proyecto | ¿Por qué se eligió? |
|--------------------------|--------------------|---------------------|
| Python 3.11 | Lenguaje backend | Estabilidad, mejoras de performance, typing moderno. |
| Django | Framework web | Productividad alta, ORM sólido, admin integrado para gestión rápida. |
| Django REST Framework (DRF) | API REST | Serialización robusta, paginación, filtros, permisos y ecosistema probado. |
| Gunicorn | Servidor WSGI | Estándar de facto para producción Python, simple y estable. |
| Next.js (App Router) | Framework React + SSG/ISR | SEO, rendimiento en edge, híbrido SSR/SSG e incremental revalidation. |
| React 18 | Base UI | Hooks concurrentes, ecosistema amplio. |
| Chakra UI | Librería de componentes | Theming rápido, accesibilidad lista, DX clara. |
| TypeScript | Tipado frontend | Escalabilidad y prevención de errores. |
| PostgreSQL 15 | Base de datos relacional | Integridad relacional, JSONB para datos semiestructurados, extensiones (trigram, full-text). |
| Redis | Cache / Cola | Latencia muy baja para caching y broker de Celery. |
| Celery | Tareas asíncronas | Manejo de jobs recurrentes y reintentos (noticias, embeddings, métricas). |
| Celery Beat | Programador | Agenda periódica (ej: refresh de noticias cada 6h). |
| n8n | Automatización / ETL | Enfoque low-code para scraping / ingest sin escribir pipelines manuales. |
| JWT (SimpleJWT) | Autenticación API | Stateless, compatible con SPA y escalable horizontalmente. |
| HuggingFace Transformers (plan) | NLP open-source | Flexibilidad para modelos locales y reducción de lock-in. |
| OpenAI API (plan) | Embeddings / resumen | Alta calidad inicial para prototipos rápidos. |
| FAISS / Qdrant (plan) | Vector store | Búsqueda semántica eficiente de embeddings. |
| Pytest + pytest-django | Testing backend | Sintaxis clara, fixtures poderosas, ejecución rápida en CI. |
| React Query (plan) | Data fetching | Cache normalizado de peticiones, gestión de estados remotos simplificada. |
| Docker + Compose | Orquestación local | Reproducibilidad entre entornos y onboarding rápido. |
| GitHub Actions (plan) | CI/CD | Automatización de tests, builds y despliegues sin infraestructura adicional. |
| Render / Railway (plan) | PaaS Deploy | Despliegue rápido, soporte para servicios web + workers + cron. |
| Sentry (plan) | Observabilidad de errores | Alertas y trazabilidad de problemas en producción. |
| Prometheus (plan) | Métricas | Recolección y monitoreo de series temporales (rendimiento, jobs). |

### Principios de Selección
1. Productividad vs. complejidad: elegir herramientas maduras que aceleren el MVP (Django, DRF, Redis, Celery).
2. Escalabilidad progresiva: planificar migraciones (TypeScript, vector DB) sin bloquear desarrollo temprano.
3. Apertura y flexibilidad: preferencia por estándares y open-source (Django, Postgres, HuggingFace) con opción a APIs gestionadas (OpenAI) para acelerar experimentación.
4. Separación de responsabilidades: automatización (n8n), ejecución diferida (Celery), API core (Django), presentación (React/Vite).
5. Observabilidad temprana planificada: definir Sentry/Prometheus desde documentación aunque se incorporen después.

### Roadmap de Adopción (Resumen)
- Fase 1 (MVP): Django + DRF + Postgres + Next.js (SSG/ISR) + Chakra + Docker.
- Fase 2: Celery + n8n + ingestas + embeddings iniciales (API externa).
- Fase 3: Búsqueda semántica (FAISS/Qdrant) + modelos locales + observabilidad.

> Nota: Las tecnologías marcadas como (plan) no deben implementarse sin requerimiento explícito para evitar sobreingeniería prematura.

---

## 🧭 Arquitectura General

```
React (Frontend) ──> Django REST API ──> PostgreSQL
       │                      │
       │                      ├── Celery + Redis → Jobs automáticos (noticias, alertas)
       │                      └── AI Pipelines → NLP, embeddings, clasificación
       │
       └── n8n (integraciones externas, ETL, scraping controlado)
```

---

## 🔍 Flujo de Búsqueda de Herramientas (Diseño Funcional)

Esta sección describe cómo funcionará la búsqueda de herramientas de IA desde que un usuario introduce una consulta hasta que se muestran los resultados. Se distinguen fases: MVP (fase textual) y evolución (fase semántica / recomendaciones).

### 1. Entrada del Usuario (Frontend)
- El usuario ingresa texto en un campo de búsqueda y selecciona filtros (categoría, tag, pricing, destacado, orden).
- El frontend construye una URL con query params, p.ej:
  `GET /api/tools/?search=vector&category=nlp&tag=embeddings&pricing=free&page=1`

### 2. API Gateway (Django REST Framework)
- Endpoint: `GET /api/tools/`
- DRF aplica:
  - Paginación (default 20)
  - Filtros (`django-filter`) en categoría, tags, pricing
  - Búsqueda (`SearchFilter`) sobre campos: `name`, `description`, `tags__name` (MVP)
  - Orden por `-created_at` (default) o `?ordering=score` (cuando se añada ranking compuesto)

### 3. Capa de Query (MVP)
- ORM genera JOINs contra tablas `Tool`, `Category`, `Tag`.
- Búsqueda textual básica: `ILIKE` o `trigram similarity` (cuando se habilite extensión) para relevancia inicial.
- Resultado: subconjunto paginado + `count` global.

### 4. Capa de Ranking (Evolución)
Futuro algoritmo de score combinado:
| Factor | Fuente | Notas |
|--------|--------|-------|
| Relevancia textual | Postgres (ts_rank / trigram) | Peso base |
| Similaridad semántica | Vector store (FAISS/Qdrant) | Embeddings (name+description) |
| Popularidad | Métricas (uso, clics) | Normalización 0-1 |
| Calidad | Rating promedio | Penaliza baja valoración |

`score_final = w_t * text + w_s * semantic + w_p * popularity + w_r * rating`

Si el vector store falla → fallback a sólo relevancia textual.

### 5. Caching e Invalidez
- Resultados de queries frecuentes (`search + filtros + page`) se almacenan en Redis (TTL corto, ej. 300s).
- Invalidez selectiva tras creación/actualización de herramienta o tarea Celery de recomputación (`refresh_tool_stats`).

### 6. Serialización
Respuesta JSON (ejemplo previsto):
```json
{
  "count": 124,
  "next": "http://localhost:8000/api/tools/?search=vector&page=2",
  "previous": null,
  "results": [
    {
      "name": "VectorAI Toolkit",
      "slug": "vectorai-toolkit",
      "description": "Librería para búsqueda semántica y embeddings.",
      "categories": [{"name": "NLP", "slug": "nlp"}],
      "tags": [{"name": "embeddings", "slug": "embeddings"}],
      "pricing": "free",
      "score": 0.8421,
      "created_at": "2025-10-05T12:30:00Z"
    }
  ]
}
```

### 7. Renderizado Frontend
- El frontend consume la respuesta y despliega tarjetas (`ToolCard`).
- Destaca términos buscados (fase futura: resaltado textual o snippet generado por embeddings + chunk summarization).
- Controles de paginación inferiores (botones, número de página).

### 8. Telemetría y Mejora Continua (Futuro)
- Clicks sobre resultados → registrados para ajustar `popularity`.
- Tiempos de permanencia → señales de calidad de resultado.
- Failover y métricas de latencia reportadas a Sentry / Prometheus.

### 9. Tareas Asíncronas Relevantes
| Tarea | Objetivo | Frecuencia |
|-------|----------|------------|
| `refresh_tool_stats` | Recalcular métricas (popularidad, rating agregado) | Cada 1h / on-demand |
| `compute_embeddings_for_new_tool` (plan) | Generar vector y guardar en store | On create |
| `rebuild_vector_index` (plan) | Re-index global (mantenimiento) | Diario |

### 10. Flujo Resumido (Texto)
```
Usuario → (Query+Filtros) → Frontend construye URL → /api/tools/ → DRF filtros + búsqueda → DB (texto) + (vector store opcional) → Combina scores → Cache Redis → Respuesta JSON → Render ToolCard → (Telemetry en background)
```

### 11. Estrategia de Degradación
| Fallo | Acción | Impacto |
|-------|-------|---------|
| Vector store down | Omitir score semántico | Resultados menos precisos |
| Redis down | Ejecutar consulta directa | + Latencia |
| Postgres lenta | Timeout → 504 | Mostrar mensaje de reintento |
| Embeddings retrasados | Score semántico nulo temporal | Ranking parcial |

### 12. Hoja de Ruta Técnica Búsqueda
1. (MVP) Filtros + búsqueda textual básica + paginación.
2. Trigram / full-text + indexación GIN.
3. Generación embeddings + vector store (FAISS local o Qdrant).
4. Fusion ranking multi-factor + caching Redis.
5. Telemetría y ajuste dinámico de pesos.
6. Recomendaciones personalizadas (perfil usuario + similitud herramientas).

---

---

## 🏗️ Fases de Desarrollo

| Fase | Descripción | Duración |
|------|--------------|-----------|
| **1️⃣ Definición (MVP)** | Diseño del modelo de datos, API base, interfaz inicial | Semanas 1–2 |
| **2️⃣ Automatización** | Ingesta automática de herramientas y noticias con n8n y Celery | Semanas 3–4 |
| **3️⃣ Inteligencia** | Implementación de IA: recomendaciones, resúmenes, alertas | Semanas 5–6 |

---

## 📈 Indicadores de Éxito (KPI)

- 📊 Número de herramientas registradas y consultas activas.  
- 👥 Porcentaje de usuarios con interacción semanal.  
- ⚡ Tiempo promedio de respuesta en búsquedas.  
- 💬 Nivel de satisfacción con las recomendaciones.  
- 🔄 Frecuencia y precisión de las actualizaciones automáticas.

---

## 🌐 Integración de Automatización (n8n)
- **Tareas automáticas:** actualización de herramientas, clasificación y feeds de noticias.  
- **Workflows programados:** obtención diaria de datos y envío al backend vía API.  
- **Enriquecimiento de datos:** etiquetas, categorías y deduplicación automatizada.  

---

## 🐳 Docker y Contenedorización

El proyecto utiliza **Docker** para contenerizar tanto el **backend (Python/Django)** como el **frontend (React/Next.js)**, junto con servicios auxiliares como **PostgreSQL**, **Redis**, **Celery Worker**, **Celery Beat** y **n8n** (automatización).  
Esto garantiza entornos reproducibles, despliegues simples y escalabilidad.

### 📁 Estructura de Proyecto
```
ai-tools-directory/
├── backend/              # Django + Celery + Redis
│   ├── Dockerfile
│   └── ...
├── frontend/             # React / Next.js
│   ├── Dockerfile
│   └── ...
├── n8n/                  # Orquestador de flujos automatizados
├── docker-compose.yml
└── README.md
```

### 🐍 Backend – `backend/Dockerfile`
```dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### ⚛️ Frontend – `frontend/Dockerfile`
```dockerfile
FROM node:20-alpine

WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install --production

COPY . .
RUN npm run build

CMD ["npm", "run", "start"]
```

### 🧩 `docker-compose.yml` (extracto actualizado)
```yaml
services:
  backend:
    build: ./backend
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000
    env_file:
      - ./.env
      - ./backend/.env  # opcional overrides
    depends_on: [db, redis]
    ports: ["8000:8000"]

  frontend:
    build: ./frontend
    env_file: [./.env]
    depends_on: [backend]
    ports: ["3000:3000"]

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    env_file: [./.env]

  redis:
    image: redis:alpine

  celery:
    build: ./backend
    command: celery -A config worker -l info
    env_file: [./.env, ./backend/.env]
    depends_on: [backend, redis]

  celery_beat:
    build: ./backend
    command: celery -A config beat -l info
    env_file: [./.env, ./backend/.env]
    depends_on: [backend, redis]

  n8n:
    image: n8nio/n8n
    env_file: [./.env]
    ports: ["5678:5678"]
```

### 🚀 Ejecución del Proyecto (Guía Docker Paso a Paso)

Esta guía sirve para que cualquier miembro del equipo ponga el stack completo en marcha rápidamente.

#### 0. Prerrequisitos
- Docker Engine + Docker Compose Plugin (≥ 24.x)
- (Opcional) Node 18+ / npm (solo si vas a desarrollar frontend fuera de contenedor)
- (Opcional) Python 3.11 local (solo si inspeccionas el backend fuera de Docker)

Verifica:
```bash
docker --version
docker compose version
```

#### 1. Clonar el repositorio
```bash
git clone https://github.com/alexormx/ai-tools-directory.git
cd ai-tools-directory
```

#### 2. Crear archivo `.env`
El proyecto ahora NO incluye `.env.example` (se eliminó para evitar confusión). Crea manualmente `.env` en la raíz con (ajusta valores sensibles):
```bash
cat > .env <<'EOF'
DJANGO_SECRET_KEY=django-insecure-reemplaza
DJANGO_DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1

POSTGRES_USER=ai_tools
POSTGRES_PASSWORD=change_me
POSTGRES_DB=ai_tools
DATABASE_URL=postgresql://ai_tools:change_me@db:5432/ai_tools

REDIS_URL=redis://redis:6379/0
CELERY_BROKER_URL=${REDIS_URL}
CELERY_RESULT_BACKEND=${REDIS_URL}

CORS_ALLOWED_ORIGINS=http://localhost:3000

N8N_WEBHOOK_SECRET=n8nwhk_placeholder
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=change_me_admin_pwd
N8N_BASIC_AUTH_ACTIVE=true
GENERIC_TIMEZONE=America/Mexico_City

ACCESS_TOKEN_LIFETIME_MIN=30
REFRESH_TOKEN_LIFETIME_DAYS=7

DEFAULT_PAGINATION_SIZE=20
REFRESH_FEATURED_INTERVAL_MIN=60
FETCH_NEWS_FEATURED_INTERVAL_MIN=360
CELERY_TASK_ALWAYS_EAGER=0
USE_SQLITE_FOR_TESTS=0

NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
INTERNAL_API_BASE_URL=http://backend:8000
EOF
```

Para generar un SECRET KEY seguro:
```bash
python -c "import secrets; print('django-insecure-' + secrets.token_urlsafe(48))"
```

Para generar un webhook secreto:
```bash
python -c "import secrets; print('n8nwhk_' + secrets.token_urlsafe(40))"
```

#### 3. (Opcional) Overrides específicos de backend
Si necesitas cambiar algo SOLO para backend sin tocar `.env` global:
```bash
mkdir -p backend
echo 'DJANGO_DEBUG=0' > backend/.env
```
El `docker-compose.yml` ya incluye `./backend/.env` como override opcional.

#### 4. Construir e iniciar TODOS los servicios (stack completo)
```bash
docker compose up -d --build
```
Esto levantará: Postgres, Redis, Backend (Gunicorn), Frontend (Next), Celery Worker, Celery Beat y n8n (panel en http://localhost:5678).

#### 5. Verificación rápida
```bash
docker compose ps
docker compose logs -f backend | sed -n '1,30p'
curl -s http://localhost:8000/health/  # debería retornar {"status":"ok"}
```

#### 6. Ejecutar migraciones y crear superusuario
```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
```

#### 7. Accesos
- Frontend: http://localhost:3000
- API Root (DRF browsable): http://localhost:8000/api/
- Admin Django: http://localhost:8000/admin/
- n8n: http://localhost:5678 (usuario/contraseña definidos en `.env`)
  - Ejemplo de webhook futuro: `/api/news/ingest/` con header `X-Webhook-Secret: $N8N_WEBHOOK_SECRET`

#### 8. Sembrar datos rápidos (ejemplo mínimo)
```bash
docker compose exec backend python manage.py shell -c "from catalog.models import Category,Tool; c,_=Category.objects.get_or_create(name='NLP'); Tool.objects.get_or_create(name='Demo Tool')"
```

#### 9. Ver herramientas
http://localhost:3000/tools (si añadiste datos)

#### 10. Parar contenedores conservando datos
```bash
docker compose down
```

#### 11. Parar y borrar volúmenes (RESET total)
```bash
docker compose down -v
```

#### 12. Reconstruir sólo un servicio tras cambios
```bash
docker compose build backend && docker compose up -d backend
docker compose build frontend && docker compose up -d frontend
```

#### 13. Ver logs específicos
```bash
docker compose logs -f backend
docker compose logs -f celery
docker compose logs -f celery_beat
docker compose logs -f frontend
```

#### 14. Ejecutar pruebas backend
```bash
docker compose exec backend pytest -q
```

#### 15. Ejecutar un comando Django puntual
```bash
docker compose exec backend python manage.py shell_plus  # si luego añadimos django-extensions
```

### 🔧 Comandos Frecuentes (Cheat Sheet)

| Objetivo | Comando |
|----------|---------|
| Build + up completo | `docker compose up -d --build` |
| Sólo backend (rápido al desarrollar) | `docker compose up -d db redis backend` |
| Reiniciar frontend | `docker compose restart frontend` |
| Limpiar caché imágenes huérfanas | `docker image prune -f` |
| Entrar a shell del contenedor backend | `docker compose exec backend bash` |
| Mostrar migraciones | `docker compose exec backend python manage.py showmigrations` |
| Crear nueva app Django | `docker compose exec backend python manage.py startapp <nombre>` |
| Correr Celery tarea manual | `docker compose exec backend python manage.py shell -c 'from catalog.tasks import refresh_all_featured_tools; refresh_all_featured_tools.delay()'` |

### 🛡️ Buenas Prácticas con `.env`
| Regla | Motivo |
|-------|--------|
| No commitear credenciales reales | Seguridad / secreto rota rápidamente |
| Usar sufijos `_INTERVAL_MIN` para tiempos | Legibilidad humana y conversión clara en settings |
| Separar override en `backend/.env` para DEBUG | Evitar tocar config global del equipo |

### 🧪 Flags Útiles
| Variable | Uso |
|----------|-----|
| `CELERY_TASK_ALWAYS_EAGER=1` | Ejecutar tareas sin worker (tests rápidos) |
| `USE_SQLITE_FOR_TESTS=1` | Forzar SQLite (no recomendado si dependes de Postgres features) |

### ❗ Troubleshooting
| Problema | Causa Probable | Solución |
|----------|----------------|----------|
| Backend no arranca (migraciones faltantes) | BD limpia | `docker compose exec backend python manage.py migrate` |
| Error conexión Postgres | Variables DB mal / puerto en uso | Ver logs `db` y revisar `DATABASE_URL` |
| Frontend build falla (`module not found`) | Dependencia no listada | Añadir en `package.json` y rebuild |
| `IntegrityError` en ingest | URL duplicada | Es comportamiento esperado (idempotencia) |
| Celery no ejecuta tareas | Worker no levantado | `docker compose up -d celery celery_beat` |
| Cambié `requirements.txt` y no refleja | Caché de build | `docker compose build --no-cache backend` |
| Puerto 3000/8000 ocupado | Otro proceso local | Matar proceso o ajustar puertos en compose |

### 🔐 Seguridad Básica (MVP)
- Rotar `DJANGO_SECRET_KEY` antes de primer despliegue público.
- Cambiar `N8N_BASIC_AUTH_PASSWORD` y desactivar `DJANGO_DEBUG` en producción.
- Limitar `ALLOWED_HOSTS` en entornos reales.
- Añadir HTTPS en capa de reverse proxy (futuro: Nginx / Render / Railway).

### 🌱 Roadmap DevOps Futuro
| Item | Descripción |
|------|-------------|
| Multi-stage backend Docker | Optimizar tamaño final y capa de dependencias |
| Imagen slim con wheels cache | Mejorar tiempos de build CI |
| Healthcheck extendido | Verificación DB + Redis + Celery ping |
| CI: coverage + artefactos | Reportar cobertura y linting |
| CD: despliegue automatizado | Push a Render / Railway mediante tags |

---

Accesos por defecto (resumen):
| Servicio | URL |
|----------|-----|
| Frontend | http://localhost:3000 |
| Backend API Root | http://localhost:8000/api/ |
| Health | http://localhost:8000/health/ |
| Admin Django | http://localhost:8000/admin/ |
| n8n | http://localhost:5678 |

---

## 🖌️ Theming & Experiencia de Administración

Se han aplicado personalizaciones para mejorar la UX del equipo interno sin añadir dependencias pesadas de terceros (opcional agregar Jazzmin más adelante si se requiere UI más avanzada):

### 1. Admin Django
- Archivo base override: `backend/templates/admin/base_site.html` (branding y CSS custom).
- Estilos principales: `backend/static/css/admin_custom.css`.
- Página de login personalizada (gradiente + glass effect): `backend/templates/admin/login.html` usando `admin_login.css`.
- Dashboard con métricas rápidas (conteos de herramientas, categorías, tags, noticias):
  - Template: `backend/templates/admin/index.html`
  - CSS: `backend/static/css/admin_dashboard.css`
  - Context processor: `config.context_processors.dashboard_metrics` (archivo `backend/config/context_processors.py`).

### 2. DRF Browsable API
- Override de template: `backend/templates/rest_framework/base.html`.
- Estilos: `backend/static/css/api_theme.css` (navbar con gradiente y tipografía mejorada).

### 3. WhiteNoise / Estáticos
- Activado `whitenoise.middleware.WhiteNoiseMiddleware` para servir estáticos comprimidos y con hash en producción (`CompressedManifestStaticFilesStorage`).
- Directorios añadidos: `static/` (fuentes, CSS), `templates/`.
- Comando de recolección:
```bash
docker compose exec backend python manage.py collectstatic --noinput
```

### 4. Extensiones Futuras (Opcional)
| Idea | Descripción | Estado |
|------|-------------|--------|
| Jazzmin | Tema avanzado con iconografía y layout mejorado | Pendiente (decisión futura) |
| Panel React Interno | Dashboard Next.js protegido con JWT | Planificado |
| Métricas en Tiempo Real | Widgets con Celery + Redis cache | Planificado |

### 5. Beneficios Logrados
| Mejora | Impacto |
|--------|---------|
| Branding consistente | Identidad visual interna clara |
| Métricas en dashboard | Visión rápida del estado de datos |
| Estética login | Mejor adopción y percepción profesional |
| Theming DRF | Navegación API más agradable para devs |
| Infra de estáticos optimizada | Menos complejidad para despliegues iniciales |

### 6. Modo Dev: Auto-Login Temporal del Admin
Para acelerar iteraciones en desarrollo se habilitó un middleware opcional que inicia sesión automáticamente en `/admin/` cuando:
```
DJANGO_DEBUG=1
DISABLE_ADMIN_AUTH=1
```
Archivo: `backend/config/middleware.py` (`AutoAdminLoginMiddleware`).

Comportamiento:
- Si no existe un superusuario crea `devadmin` con password inseguro local `devpassword123`.
- Evita el formulario de login mientras el flag está activo.
- No usar en producción (poner `DISABLE_ADMIN_AUTH=0`).

Desactivar:
```
DISABLE_ADMIN_AUTH=0
docker compose restart backend
```

Luego el formulario de login personalizado vuelve a mostrarse (`backend/templates/admin/login.html`).

---

## 🔄 Resumen de Cambios Recientes (Changelog Interno)
| Commit (mensaje resumido) | Descripción |
|---------------------------|-------------|
| feat(admin): estilizado básico... | Override base_site + CSS inicial admin |
| feat(admin+api): dashboard métricas... | Login custom, métricas, theming DRF |

> Para ver histórico completo: `git log --oneline --decorate --graph -n 15`

---

### Variables de Entorno Clave
| Nombre | Uso |
|--------|-----|
| DJANGO_SECRET_KEY | Seguridad Django |
| POSTGRES_USER / PASSWORD / DB | Credenciales BD |
| DATABASE_URL | Conexión unificada a Postgres |
| REDIS_URL | Broker/resultado Celery |
| CORS_ALLOWED_ORIGINS | Fuentes permitidas frontend |
| N8N_WEBHOOK_SECRET | Validación ingest de noticias |
| N8N_BASIC_AUTH_USER / PASSWORD | Acceso panel n8n |
| NEXT_PUBLIC_API_BASE_URL | Base pública fetch frontend |
| INTERNAL_API_BASE_URL | Base interna SSR (opcional) |
| DEFAULT_PAGINATION_SIZE | Config paginación API |
| REFRESH_FEATURED_INTERVAL_MIN | Minutos entre refresh de herramientas destacadas |
| FETCH_NEWS_FEATURED_INTERVAL_MIN | Minutos entre fetch de noticias destacadas |
| CELERY_TASK_ALWAYS_EAGER | Ejecutar tareas sin worker (tests) |
| USE_SQLITE_FOR_TESTS | Forzar SQLite en tests |

> Nunca commit de valores reales sensibles. `.env` está en `.gitignore`.

---

## 🤝 Visión del Equipo
El proyecto **AI Tools Directory** representa una **iniciativa colaborativa** orientada a aplicar conocimientos de **Inteligencia Artificial, desarrollo web y automatización** en un entorno práctico.  

El equipo busca construir una **plataforma viva, inteligente y en evolución constante**, que demuestre la capacidad técnica conjunta para diseñar soluciones modernas basadas en datos, IA y experiencia de usuario.

---

## 🧩 Repositorios y Colaboración
- **Backend (Django REST API):** `/backend`  
- **Frontend (React / Next.js):** `/frontend`  
- **n8n Workflows:** `/automations`  
- **AI Pipelines:** `/ai_pipelines`  
- **Documentación:** `/docs`

---

## 📬 Contacto del Equipo AI MAVERIC

**Integrantes:**  
- **Alejandro Ortiz López** – [alexormx@gmail.com](mailto:alexormx@gmail.com)  
- **Marco Navarro** – [arcoa05tony@gmail.com](mailto:arcoa05tony@gmail.com)  
- **José Roberto Escamilla Meza** – [escamillamezaj@gmail.com](mailto:escamillamezaj@gmail.com)  

**Repositorio oficial:**  
🔗 [https://github.com/alexormx/ai-tools-directory](https://github.com/alexormx/ai-tools-directory)

🧠 Proyecto académico – Octubre 2025  

---
