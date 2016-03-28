import urllib

from django.apps import apps
from django.conf import settings
from django.core.urlresolvers import reverse


def breadcrumb():
    all_apps = settings.INSTALLED_APPS
    app_list = []
    app_models = []

    for app in all_apps:
        if 'fifa.' in app:
            app_list.append(app.replace('fifa.apps.', ''))

    for app in app_list:
        app_models = apps.get_app_config(app).get_models()

        for model in app_models:
            print(model)


def build_url(*args, **kwargs):
    request = kwargs.pop('request', {})
    get = kwargs.pop('get', {})
    remove = kwargs.pop('remove', '')
    url = ''

    # Sometimes no 'viewname' is passed i.e. building pagination links
    if args or kwargs:
        url = reverse(*args, **kwargs)

    if hasattr(request, 'dict'):
        params = request.dict()

        # If we want to change something more than likely we want to
        # reset the current page, so remove the page param
        if 'page' in params and get:
            params.pop('page')

        if remove:
            for item in remove:
                params.pop(item, None)

        params.update(**get)

        url += '?{}'.format(urllib.parse.urlencode(params))

    return url
