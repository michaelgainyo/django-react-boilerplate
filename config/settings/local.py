from .base import *

SECRET_KEY = 'my-secret-key-goes-here'

CORS_ORIGIN = 'http://localhost:3000'

DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MIDDLEWARE = [
    # CORS
    'config.middleware.CORSMiddleware',

    *MIDDLEWARE,
]

# MEDIA & STATIC

STATIC_URL = '/static/'
STATICFILES_DIRS = [BUILD_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
