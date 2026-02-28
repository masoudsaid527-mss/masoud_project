import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

# Set debug to False in production
DEBUG = False

# Set ALLOWED_HOSTS to your domain
# Use Render-provided hostname or default to localhost
ALLOWED_HOSTS = [
    "masoud-project-64gt.onrender.com",
]

# Recommended for CSRF protection (e.g. for forms)
CSRF_TRUSTED_ORIGINS = [
    "https://my-project-eexs.vercel.app",
]

# Secret key must be set in environment variable
SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-default')

# Middleware for production
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Static files config for WhiteNoise
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Parse DATABASE_URL from Render (PostgreSQL)
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        # ssl_require=True  # important for Render PostgreSQL
    )
}

# CORS for React frontend (update to your actual frontend URL)
CORS_ALLOWED_ORIGINS = [
    "https://my-project-eexs.vercel.app",
]

CORS_ALLOW_CREDENTIALS = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SAMESITE = "None"

# Storages configuration
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    }
}
