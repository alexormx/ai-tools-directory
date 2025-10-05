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

Esta sección describe la estrategia integral para: (1) descubrir y recolectar nuevas herramientas y noticias de IA, (2) normalizar y enriquecer los datos, y (3) aplicar un flujo de aprobación manual antes de su publicación pública.

### 🎯 Objetivos de la Ingesta
1. Capturar señales relevantes (herramientas, lanzamientos, noticias, artículos técnicos) con latencia baja (≤ 6h en MVP).
2. Evitar duplicados y ruido (spam, contenido comercial irrelevante).
3. Enriquecer cada item con metadatos consistentes (categorías, tags, resumen, origen, puntuaciones de calidad).
4. Permitir un punto de control humano (moderación) antes de exposición pública.
5. Mantener trazabilidad de fuente, primer avistamiento y últimos refrescos.

### 🗂️ Tipos de Contenido
| Tipo | Descripción | Ejemplos de Campos Core |
|------|-------------|--------------------------|
| Tool Discovery | Nuevas herramientas / plataformas de IA | name, url, description_raw, pricing_raw, source, categories_sugeridas |
| News / Article | Noticias, posts de blog, investigaciones | title, url, published_at, excerpt_raw, source, topics_sugeridos |
| Release Notes (futuro) | Cambios en herramientas conocidas | tool_slug, version, notes_raw |
| Dataset (futuro) | Publicación de dataset relevante | name, url, modality, license |

### 🔎 Fuentes Planeadas (Agrupadas)
| Grupo | Fuentes (Ejemplos) | Método | Frecuencia |
|-------|--------------------|--------|-----------|
| RSS / Syndication | HuggingFace blog, OpenAI blog, Stability, Google AI | RSS Poll | 30–60 min |
| Curated Listings | Product Hunt (categorías IA), BetaList | API / HTML parse (n8n + limit) | 2–3 h |
| Code & Repos | GitHub Trending (topics: ai, llm, nlp, cv) | API/HTML + filtro stars | 6 h |
| Community Signals | Hacker News (keywords: LLM, AI, OpenAI, model) | Algolia API | 1 h |
| Vendor Changelogs | OpenAI / Anthropic / Replicate changelogs | RSS / HTML diff | 6 h |
| Newsletters (futuro) | Import manual + parsing estructurado | Email -> Parse | Diario |
| Research (futuro) | arXiv cs.AI / ML | API arXiv | Diario |

> Nota: Toda fuente con scraping HTML debe respetar robots.txt y límites de 1 req/seg (configurable en n8n). Si una fuente ofrece API oficial, se prefiere API.

### 🧬 Pipeline Lógico (Stages)
1. Fetch bruto (pull) o recepción (webhook) → item(s) crudos.
2. Normalización (campos uniformes): slugify, limpiar HTML, truncar longitudes.
3. Deduplicación: hash SHA256 de `canonical_url` + tipo. Si existe → actualizar `last_seen_at`.
4. Enriquecimiento:
   - Extracción metadatos (OpenGraph / `<meta>`).
   - Limpieza de descripciones (strip markdown).
   - Clasificación categorías (Zero-Shot) → top N con score ≥ umbral.
   - Extracción tags clave (RAKE / KeyBERT / embeddings plan futuro).
   - Resumen (modelo ligero primero, luego LLM si > umbral tamaño).
   - Detección de idioma (descartar no-EN/ES en MVP configurable).
5. Scoring preliminar: heurística (longitud título, reputación fuente, signals sociales si disponibles).
6. Persistencia en estado `draft` (no público).
7. Moderación manual (admin): aprobar / rechazar / editar.
8. Publicación → visible en APIs públicas y frontend (ISR revalidate).

### 🧾 Estados del Ciclo de Vida
| Estado | Transición Desde | Transición A | Descripción |
|--------|------------------|-------------|-------------|
| draft | ingest inicial | pending_review (opcional), rejected | Item recién ingresado y enriquecido automáticamente. |
| pending_review | draft | published, rejected | Marcado para revisión humana (batch). |
| rejected | draft/pending_review | (reopen manual) | No cumple criterios (spam, duplicado conceptual, baja calidad). |
| published | pending_review | (unpublish manual) | Visible en API pública y frontend. |

### 👩‍💻 Moderación Manual
Se gestionará inicialmente vía Django Admin:
- Filtros: estado, tipo, fuente, fecha ingest, score heurístico.
- Acciones masivas: aprobar lote, rechazar lote, recalcular enriquecimiento.
- Vista detalle: diff de enriquecimiento (versión previa vs regenerada) futura.

### 🔐 Seguridad de la Ingesta
| Aspecto | Implementación |
|---------|----------------|
| Autenticación webhook | Header `X-Webhook-Secret: $N8N_WEBHOOK_SECRET` |
| Idempotencia | Hash de URL + tipo como clave natural |
| Rate limiting (futuro) | Redis counter per source |
| Sanitización | Escape/strip HTML antes de almacenar |
| Validación URL | `http(s)` + longitud < 500 + dominio permitido opcional |

### ♻️ Idempotencia & Deduplicación
Pseudo algoritmo:
```
canonical_url = normalizar(url)
key_hash = sha256(tipo + '::' + canonical_url)
if existe(key_hash): update last_seen_at, merge campos vacíos -> existentes
else: crear registro nuevo (estado=draft)
```

### 🧪 Validaciones Automáticas (Pre-Publicación)
| Chequeo | Regla | Acción |
|---------|-------|-------|
| Longitud título | 5 ≤ palabras ≤ 24 | Flag warning si falla |
| Descripción vacía | Obligatoria (≥ 40 chars post limpieza) | Regenerar intento/resumen |
| Dominio bloqueado | Lista negra (config) | Rechazar directo |
| Idioma | es/en | Marcar para revisión si diferente |
| Duplicado semántico (futuro) | similitud > 0.93 embeddings | Merge / marcar duplicado |

### 🛠️ Estructura de Workflows n8n (Convenciones)
| Prefijo | Propósito | Ejemplo |
|---------|----------|---------|
| `tools_` | Descubrimiento herramientas | `tools_producthunt_scan` |
| `news_` | Noticias / artículos | `news_rss_ai_blogs` |
| `enrich_` | Enriquecimiento batch | `enrich_recompute_summaries` |
| `sync_` | Mantenimiento / housekeeping | `sync_reindex_daily` |

Variables críticas (en `.env` / n8n env panel):
`N8N_WEBHOOK_SECRET`, límites de requests, claves API externas (no se commitean).

### 🧵 Campos de Datos Normalizados (MVP)
| Campo | Tool | News | Descripción |
|-------|------|------|-------------|
| name/title | ✓ | ✓ | Texto principal |
| slug | ✓ | (derivado) | Slug único para URL interna |
| url | ✓ | ✓ | Enlace canónico |
| source_kind | ✓ | ✓ | rss, api, scrape, manual |
| source_name | ✓ | ✓ | Identificador humano ("producthunt", "openai_blog") |
| description_raw | ✓ | (opcional) | Texto original antes de resumen |
| excerpt_raw | - | ✓ | Extracto original noticia |
| summary | ✓ | ✓ | Resumen generado / validado |
| categories | ✓ | (tags) | Lista sugerida (hasta 5) |
| tags | ✓ | ✓ | Palabras clave |
| published_at | (opcional) | ✓ | Fecha original |
| discovered_at | ✓ | ✓ | Fecha primera ingest |
| last_seen_at | ✓ | ✓ | Última vez que la fuente lo listó |
| status | ✓ | ✓ | Workflow state |
| quality_score | ✓ | ✓ | 0–1 heurístico |
| external_id | ✓ | ✓ | ID de fuente si disponible |
| url_hash | ✓ | ✓ | SHA256 dedupe |

### 🔄 Frecuencias de Ejecución (Propuesta MVP)
| Grupo | Frecuencia | Mecanismo |
|-------|-----------|-----------|
| RSS blogs IA | 30 min | Cron n8n |
| Product Hunt IA | 3 h | Cron + filtro categoría |
| GitHub trending | 6 h | Cron + topics & stars > X |
| Hacker News keywords | 60 min | Cron (Algolia API search) |
| Re-enriquecimiento (score bajo) | 12 h | Celery task (futuro) |

### 🧱 Flujo End-to-End (Resumen Textual)
```
Fuente → n8n fetch → Normalización → Hash & Dedupe → Enriquecimiento → Persist draft → (Opcional: heurística marca pending_review) → Moderador aprueba → Publicación → Frontend revalida
```

### 📨 Payload Webhook Ejemplo (Noticias)
```json
{
  "type": "news",
  "title": "OpenAI lanza nueva API de embeddings",
  "url": "https://openai.com/blog/new-embeddings",
  "published_at": "2025-10-05T09:30:00Z",
  "source_kind": "rss",
  "source_name": "openai_blog",
  "excerpt_raw": "Today we introduce a more efficient embedding model...",
  "topics_sugeridos": ["embeddings", "nlp"],
  "external_id": "openai_blog_20251005_0930"
}
```

Respuesta (idempotente):
```json
{ "status": "accepted", "id": 418, "state": "draft", "duplicate": false }
```

Si duplicado:
```json
{ "status": "accepted", "id": 418, "state": "draft", "duplicate": true }
```

### ✅ Criterios para Publicación Automática (Opcional Futuro)
Activar sólo cuando la precisión del enriquecimiento alcance umbral aceptable (>90% validaciones manuales):
| Regla | Parámetro |
|-------|-----------|
| quality_score ≥ | 0.75 |
| idioma permitido | es/en |
| categorías confiables | ≥ 1 con score > 0.6 |
| resumen generado | no vacío |
| no flagged spam | true |

### 📊 Métricas & Observabilidad (Futuro)
| Métrica | Descripción |
|---------|-------------|
| ingest_items_total | Conteo acumulado por tipo |
| ingest_duplicates_total | Items descartados por hash |
| enrichment_fail_total | Errores en etapa de enriquecimiento |
| moderation_pending | Items pendientes revisión |
| publish_latency_seconds | (published_at - discovered_at) |

### 🗺️ Roadmap Fases Ingesta
| Fase | Enfoque | Alcance |
|------|---------|---------|
| MVP | RSS + ProductHunt (limitado) | Tools + News básicos, moderación manual |
| F2 | Añadir HackerNews + GitHub trending | Ampliar descubrimiento técnico |
| F3 | Embeddings para dedupe semántico | Reducción de casi-duplicados |
| F4 | Auto-publicación condicionada | Reglas + monitoreo precisión |
| F5 | Panel moderador dedicado (frontend) | UX mejorada fuera del admin |

### 🧪 Testing Estratégico (A implementar)
| Test | Objetivo |
|------|----------|
| POST /api/news/ingest sin secreto | Rechazo 401 |
| POST /api/news/ingest duplicado | 200 + duplicate=true |
| Normalización URL | Eliminar trailing slashes/query ruido |
| Hash consistente | Mismo URL distinto orden query → mismo hash |
| Estados moderación | Transiciones válidas únicamente |

### 🧾 Resumen Clave
- n8n actúa como capa de orquestación (fetch + pre-procesado ligero).
- El backend centraliza persistencia, dedupe, estados y moderación.
- Manual first: publicar sólo tras revisión en primeras fases para garantizar calidad.
- Arquitectura preparada para evolucionar a publicación semi-automática basada en score.
- Toda comunicación entrante autenticada vía secreto y diseñada idempotente.

> Esta estrategia minimiza riesgo de spam, mantiene calidad editorial inicial y permite escalar progresivamente complejidad de enriquecimiento e inteligencia.

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
curl -s http://localhost:8000/health/  # debería retornar {"status":"ok","components":{"db":true,"redis":true,"celery":true}}
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
- Reutiliza un superusuario existente si lo hay.
- NO crea usuarios con credenciales hardcodeadas en el repositorio.
- Creación automática opcional sólo si defines en `.env` además:
  - `CREATE_DEV_SUPERUSER=1`
  - `DEV_SUPERUSER_NAME=admin_local` (ejemplo)
  - `DEV_SUPERUSER_EMAIL=admin@example.com`
  - `DEV_SUPERUSER_PASSWORD=una_password_segura`
- Si `CREATE_DEV_SUPERUSER` no está activo y no hay superusuario, se mostrará el login normal.
- No usar en producción (poner `DISABLE_ADMIN_AUTH=0` y no exponer las variables anteriores).

Desactivar:
```
DISABLE_ADMIN_AUTH=0
docker compose restart backend
```

Luego el formulario de login personalizado vuelve a mostrarse (`backend/templates/admin/login.html`).

### 7. Health Endpoint Extendido
El endpoint `/health/` ahora devuelve un JSON con el estado de componentes críticos:
```json
{
  "status": "ok",          // o "degraded" si algún componente falla
  "components": {
    "db": true,
    "redis": true,
    "celery": true
  }
}
```
Código fuente: `catalog/views.py` función `health`.
Estados:
- `ok`: todos los componentes respondieron.
- `degraded` (HTTP 503): uno o más componentes fallaron (no detiene la app, sirve como alerta temprana).

---

## 🔄 Resumen de Cambios Recientes (Changelog Interno)
| Commit (mensaje resumido) | Descripción |
|---------------------------|-------------|
| feat(admin): estilizado básico... | Override base_site + CSS inicial admin |
| feat(admin+api): dashboard métricas... | Login custom, métricas, theming DRF |
| fix(admin-login): restaurado formulario | Se reintroduce el form de autenticación manual |
| feat(health): endpoint extendido | Chequeos DB/Redis/Celery y test actualizado |
| fix(health): detección Celery | Chequeo genérico del registro de tareas |
| feat(dev): middleware auto-login | Inserción condicional según DISABLE_ADMIN_AUTH |
| fix(admin): eliminar extends duplicado | Limpieza de template index admin |
| chore(dev): refactor variable interna | Variable `_disable_admin` en settings |
| chore(auth-dev): parametrizar auto-login | Variables de entorno para crear superuser dev |

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
| DISABLE_ADMIN_AUTH | (Dev) Activar auto-login admin sin formulario |
| CREATE_DEV_SUPERUSER | (Dev) Crear superusuario si no existe (1/0) |
| DEV_SUPERUSER_NAME | (Dev) Nombre del superusuario a crear |
| DEV_SUPERUSER_EMAIL | (Dev) Email del superusuario a crear |
| DEV_SUPERUSER_PASSWORD | (Dev) Password del superusuario (no commitear) |

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
