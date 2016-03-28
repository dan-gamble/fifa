# flake8: noqa

from __future__ import absolute_import

from .base import *

import environ

env = environ.Env()

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

INSTALLED_APPS += ('opbeat.contrib.django',)
OPBEAT = {
    'ORGANIZATION_ID': env('DJANGO_OPBEAT_ORGANIZATION_ID'),
    'APP_ID': env('DJANGO_OPBEAT_APP_ID'),
    'SECRET_TOKEN': env('DJANGO_OPBEAT_SECRET_TOKEN')
}

MIDDLEWARE_CLASSES = (
     'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
 ) + MIDDLEWARE_CLASSES

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['futily.com'])
# END SITE CONFIGURATION

INSTALLED_APPS += ("gunicorn",)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER

CACHES = {}

SECRET_KEY = env('SECRET_KEY')

CORS_ORIGIN_WHITELIST = ()

# Cache templates
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
