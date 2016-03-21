from __future__ import absolute_import

from django.contrib.staticfiles.storage import staticfiles_storage
from jinja2 import Environment

from fifa.utils.urls import build_url


def environment(**options):
    env = Environment(**options)

    env.globals.update({
        'static': staticfiles_storage.url,
        'url': build_url
    })

    return env
