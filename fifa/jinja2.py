from __future__ import absolute_import

from django.contrib.staticfiles.storage import staticfiles_storage
from jinja2 import Environment

from fifa.utils.globals import breadcrumb, build_url
from fifa.utils.filters import color_string


def environment(**options):
    env = Environment(**options)

    env.globals.update({
        'static': staticfiles_storage.url,
        'url': build_url,
        'breadcrumb_urls': breadcrumb
    })

    env.filters.update({
        'color_string': color_string
    })

    return env
