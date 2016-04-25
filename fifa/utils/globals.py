import urllib

from django.apps import apps
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from jinja2 import contextfunction


@contextfunction
def breadcrumb(context):
    current_obj = context.parent.get('object', None)
    url_list = [
        {
            'title': 'Home',
            'url': '/',
            'active': False
        }
    ]

    if current_obj:
        content_type = ContentType.objects.get_for_model(current_obj)
        app_label = content_type.app_label
        title = current_obj.common_name if content_type.model == 'player' else current_obj.name

        url_list.append({
            'title': app_label.capitalize(),
            'url': reverse('{}:{}'.format(app_label, app_label)),
            'active': False
        })
        url_list.append({
            'title': title,
            'url': current_obj.get_absolute_url(),
            'active': True
        })

    return url_list


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
