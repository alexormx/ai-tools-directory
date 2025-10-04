# 🧠 AI TOOLS DIRECTORY  
**Plataforma Inteligente de Herramientas y Tendencias en Inteligencia Artificial**  
Equipo de Desarrollo IA – Octubre 2025  

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
| **Frontend** | React 18 + Vite / Next.js | Interfaz dinámica y optimizada para SEO |
| **Backend** | Python 3.11 + Django REST Framework | API modular, segura y escalable |
| **Automatización** | n8n (Docker) | Ingesta de datos y flujos ETL automatizados |
| **Procesamiento Asíncrono** | Celery + Redis | Ejecución programada de tareas |
| **Base de Datos** | PostgreSQL + FAISS / Qdrant | Datos estructurados y búsqueda semántica |
| **IA / NLP** | OpenAI API + HuggingFace Transformers | Clasificación, embeddings y resúmenes |
| **Infraestructura** | Docker + GitHub Actions + Render/Heroku | CI/CD y despliegue automatizado |
| **Autenticación** | JWT + Social Auth | Seguridad y facilidad de acceso |
| **Observabilidad** | Sentry / Prometheus | Monitoreo, métricas y trazabilidad |

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

### 🧩 `docker-compose.yml`
```yaml
version: "3.9"

services:
  backend:
    build: ./backend
    container_name: ai_backend
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis
    env_file:
      - ./backend/.env

  frontend:
    build: ./frontend
    container_name: ai_frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

  db:
    image: postgres:15
    container_name: ai_postgres
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin123
      POSTGRES_DB: ai_tools
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:alpine
    container_name: ai_redis

  celery:
    build: ./backend
    command: celery -A config worker -l info
    depends_on:
      - backend
      - redis
    env_file:
      - ./backend/.env

  celery_beat:
    build: ./backend
    command: celery -A config beat -l info
    depends_on:
      - backend
      - redis
    env_file:
      - ./backend/.env

  n8n:
    image: n8nio/n8n
    container_name: ai_n8n
    ports:
      - "5678:5678"
    environment:
      - GENERIC_TIMEZONE=America/Mexico_City
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=supersecure
    volumes:
      - n8n_data:/home/node/.n8n

volumes:
  postgres_data:
  n8n_data:
```

### 🚀 Ejecución del Proyecto
```bash
# Construir e iniciar todos los contenedores
docker compose up --build
```

Accesos por defecto:  
- **Frontend:** http://localhost:3000  
- **Backend API:** http://localhost:8000  
- **n8n Dashboard:** http://localhost:5678  

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

## 📬 Contacto del Equipo

**Integrantes:**  
- **Alejandro Ortiz López** – [alexormx@gmail.com](mailto:alexormx@gmail.com)  
- **Marco Navarro** – [arcoa05tony@gmail.com](mailto:arcoa05tony@gmail.com)  
- **José Roberto Escamilla Meza** – [escamillamezaj@gmail.com](mailto:escamillamezaj@gmail.com)  

**Repositorio oficial:**  
🔗 [https://github.com/alexormx/ai-tools-directory](https://github.com/alexormx/ai-tools-directory)

🧠 Proyecto académico – Octubre 2025  

---
