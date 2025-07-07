from pathlib import Path
import os

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key (consider moving to env variable for production)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-+gi97x0qz+w0g=17(^2hq0=mmr)7o=29j4!2o3nl+&j3a9-%)x')

# Debug toggle
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"

# Custom environment variable to load dev/prod settings
DJANGO_ENV = os.getenv('DJANGO_ENV', 'dev')

if DJANGO_ENV == 'prod':
    from .settings_prod import *
else:
    from .settings_dev import *

# ✅ FIX: This line was incorrect — don't assign to ALLOWED_HOSTS twice
ALLOWED_HOSTS = ['django-task-backend.onrender.com', 'localhost', '127.0.0.1']

# ❌ REMOVE THIS LINE — it's invalid Python (caused your app to crash)
# DJANGO_ALLOWED_HOSTS = django-task-backend.onrender.com

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'django.contrib.staticfiles',
    'api',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',  # Only disable CSRF if needed
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'api.tasks.jwt_middleware.JWTMiddleware',
    'api.tasks.cors.CorsMiddleware',
    'api.doc_middleware.SwaggerAccess',
]

ROOT_URLCONF = 'task_backend.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

WSGI_APPLICATION = 'task_backend.wsgi.application'

# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Locale
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
