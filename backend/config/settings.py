import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'insecure-key')
DEBUG = os.getenv('DJANGO_DEBUG', '0') == '1'
ALLOWED_HOSTS = [h.strip() for h in os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',') if h.strip()]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'corsheaders',
    'catalog',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'config.context_processors.dashboard_metrics',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/postgres')
import dj_database_url  # type: ignore
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=60)
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
]

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = os.getenv('TZ', 'UTC')
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    # Facilita servir estáticos (incluye admin) sin necesitar collectstatic en dev
    WHITENOISE_AUTOREFRESH = True
    WHITENOISE_USE_FINDERS = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': int(os.getenv('DEFAULT_PAGINATION_SIZE', '20')),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter'
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=int(os.getenv('ACCESS_TOKEN_LIFETIME_MIN', '30'))),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(os.getenv('REFRESH_TOKEN_LIFETIME_DAYS', '7'))),
}

CORS_ALLOWED_ORIGINS = [o.strip() for o in os.getenv('CORS_ALLOWED_ORIGINS', '').split(',') if o.strip()]

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', os.getenv('REDIS_URL', 'redis://redis:6379/0'))
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', CELERY_BROKER_URL)

N8N_WEBHOOK_SECRET = os.getenv('N8N_WEBHOOK_SECRET', '')

# Celery / Beat configuration
CELERY_TASK_ALWAYS_EAGER = os.getenv('CELERY_TASK_ALWAYS_EAGER', '0') == '1'  # útil para tests locales
_refresh_featured_minutes = int(os.getenv('REFRESH_FEATURED_INTERVAL_MIN', '60'))  # 60 min = 1h
_fetch_news_featured_minutes = int(os.getenv('FETCH_NEWS_FEATURED_INTERVAL_MIN', '360'))  # 360 min = 6h
CELERY_BEAT_SCHEDULE = {
    'refresh-featured-tools': {
        'task': 'catalog.tasks.refresh_all_featured_tools',
        # Celery espera segundos; convertimos desde minutos declarados
        'schedule': _refresh_featured_minutes * 60,
    },
    'fetch-news-featured-tools': {
        'task': 'catalog.tasks.fetch_recent_news_for_featured_tools',
        'schedule': _fetch_news_featured_minutes * 60,
    },
}

# --- Dev helper: Auto login admin (seguridad: SOLO usar en local) ---
if DEBUG and os.getenv('DISABLE_ADMIN_AUTH', '0') == '1':  # pragma: no cover
    # Insertar justo después de AuthenticationMiddleware
    try:
        idx = MIDDLEWARE.index('django.contrib.auth.middleware.AuthenticationMiddleware') + 1
    except ValueError:
        idx = len(MIDDLEWARE)
    MIDDLEWARE.insert(idx, 'config.middleware.AutoAdminLoginMiddleware')

# Test friendly DB config override (pytest can set ENV to force sqlite for speed)
if os.getenv('USE_SQLITE_FOR_TESTS', '0') == '1':  # pragma: no cover
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'test_db.sqlite3'
        }
    }
