import os
from pathlib import Path
from mongoengine import connect

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# The directory where static files will be collected
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Additional locations to search for static files
STATICFILES_DIRS = [BASE_DIR / 'static']

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-07zheu5id@&!6al_wcr(vy%fgv%6f@nd!gcu8t6&&o7hy$np6a'
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "rest_framework",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',  # Add this line
    'app.apps.AppConfig',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',  # Add this line
]

ROOT_URLCONF = "PetCareBackend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "PetCareBackend.wsgi.application"

# Database (MongoDB)
MONGODB_URI = "mongodb+srv://root:database@cluster0.upnhy88.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tlsAllowInvalidCertificates=true"

connect(
    db='pet_care',
    host=MONGODB_URI
) 

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "https://pet-care-frontend-black.vercel.app",
]
