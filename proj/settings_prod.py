from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1', 'localhost')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "sidia",
        "USER": "postgres",
        "PASSWORD": "root",
        "HOST": "sidia_db",
        "PORT": "5432",
    }
}

AUTH_PASSWORD_VALIDATORS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'