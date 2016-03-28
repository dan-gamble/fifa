import urllib

from django.core.urlresolvers import reverse


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
