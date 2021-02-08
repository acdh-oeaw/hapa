import os
from .base import *

SECRET_KEY = 'some_key_not_used_in_production'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
REDMINE_ID = 123456

BASE_URL = 'https://hapa.acdh.oeaw.ac.at'

ALLOWED_HOSTS = [
    "*"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('POSTGRES_DB', 'hapa'),
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


Z_ID = "1234"
Z_LIBRARY_TYPE = "group"
Z_API_KEY = "safsdafsd"
