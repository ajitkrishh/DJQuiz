from .common import *
import os


DEBUG = False

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': int(os.environ['DATABASE_PORT']),
    }
}
