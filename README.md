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

El proyecto utiliza **Docker** para contenerizar tanto el **backend (Python/Django)** como el **frontend (React/Next.js)**, junto con servicios auxiliares como PostgreSQL, Redis, Celery y n8n.  
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

### 🚀 Ejecución del Proyecto

#### 1. Clonar y preparar variables
```bash
git clone https://github.com/alexormx/ai-tools-directory.git
cd ai-tools-directory
cp .env.example .env
```
Editar `.env` y sustituir:
- `DJANGO_SECRET_KEY` (usa comando sugerido en el archivo)
- `POSTGRES_PASSWORD`
- `N8N_WEBHOOK_SECRET`
- `N8N_BASIC_AUTH_PASSWORD`

Opcional: crear `backend/.env` para overrides específicos (ej. DEBUG diferente al frontend).

#### 2. (Temporal) Instalar dependencias frontend para generar lockfile
```bash
cd frontend
npm install
cd ..
```

#### 3. Construir e iniciar servicios
```bash
docker compose up --build -d
```

#### 4. Ver logs
```bash
docker compose logs -f frontend
docker compose logs -f backend
```

#### 5. (Backend futuro) Migraciones y superusuario
```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
```

#### 6. Parar y limpiar
```bash
docker compose down
```

Accesos por defecto:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- n8n Dashboard: http://localhost:5678

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
