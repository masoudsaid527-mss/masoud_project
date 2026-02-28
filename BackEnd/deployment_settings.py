import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

DEBUG = False

ALLOWED_HOSTS = [
    "masoud-project-64gt.onrender.com",
]

INSTALLED_APPS = [
    "corsheaders",
]

CSRF_TRUSTED_ORIGINS = [
    "https://my-project-1-re1u.onrender.com",
]

SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-default')

# ✅ Middleware order corrected
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # MUST BE FIRST
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ CORS correct spelling
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "https://my-project-1-re1u.onrender.com",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
    )
}

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    }
}
