import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

# -------------------------
# Security & Debug
# -------------------------
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-default')

# -------------------------
# Hosts & CSRF
# -------------------------
ALLOWED_HOSTS = [
    "masoud-project-64gt.onrender.com",  # Render backend domain
]

CSRF_TRUSTED_ORIGINS = [
    "https://masoudsaid527-mss-myproject.vercel.app",  # Vercel frontend domain
]

# -------------------------
# Middleware
# -------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -------------------------
# REST Framework
# -------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),
}

# -------------------------
# Database (Render PostgreSQL)
# -------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,  # recommended for Render PostgreSQL
    )
}

# -------------------------
# Static Files (WhiteNoise)
# -------------------------
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# -------------------------
# CORS (React frontend)
# -------------------------
CORS_ALLOWED_ORIGINS = [
    "https://masoudsaid527-mss-myproject.vercel.app",  # Vercel frontend
]

CORS_ALLOW_CREDENTIALS = True

# -------------------------
# Cookies (secure for cross-site)
# -------------------------
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SAMESITE = "None"
