
import environ
from pathlib import Path

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'my-secret-key-goes-here'),

    GH_DB_NAME=(str, 'postgres'),
    GH_DB_USER=(str, 'postgres'),
    GH_DB_PWD=(str, 'postgres'),
    GH_DB_HOST=(str, '127.0.0.1'),
    GH_DB_PORT=(str, '5432'),
)

environ.Env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATES_DIR = BASE_DIR / 'templates'
CLIENT_DIR = BASE_DIR / 'client'
BUILD_DIR = CLIENT_DIR / 'build'

CORS_ORIGIN = None


SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    # DJANGO

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # VENDORS
    'rest_framework',

    # MIQ
    'miq.apps.MiqConfig',

    # APPS
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

"""
# USER MODEL
"""

AUTH_USER_MODEL = 'miq.User'

"""
# SITE
"""

SITE_ID = 1


"""
LANG & LOCATION
"""

USE_TZ = True
USE_L10N = True
USE_I18N = True
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'

"""
AUTO FIELD
"""

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
