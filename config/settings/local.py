import os

from .base import *

SECRET_KEY = 'my-secret-key-goes-here'

CORS_ORIGIN = 'http://127.0.0.1:3000'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PWD'),
        'HOST': '',
        'PORT': '',
    }
}

"""
# Testing with github actions
"""

if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('GH_DB_NAME'),
            'USER': env('GH_DB_USER'),
            'PASSWORD': env('GH_DB_PWD'),
            'HOST': env('GH_DB_HOST'),
            'PORT': env('GH_DB_PORT'),
        }
    }


"""
# MIDDLEWARE
"""

MIDDLEWARE = [
    # CORS
    'miq.middleware.CORSMiddleware',

    *MIDDLEWARE,
]


"""
# REST FRAMEWORK
"""

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Set for all views
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 16,
}

# MEDIA & STATIC

STATIC_URL = '/static/'
STATICFILES_DIRS = [BUILD_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
