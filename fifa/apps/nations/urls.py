from django.conf.urls import url
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import NationViewSet

nation_list = NationViewSet.as_view({
    'get': 'list'
})
nation_detail = NationViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^nations/$', nation_list, name='nation-list'),
    url(r'^nations/(?P<pk>[0-9]+)/$', nation_detail, name='nation-detail'),
])

# from django.conf.urls import url
#
# from .views import NationList, NationDetail
#
# urlpatterns = [
#     url(r'^$', NationList.as_view(), name='nations'),
#     url(r'^(?P<slug>[\w-]+)/$', NationDetail.as_view(), name='nation')
# ]
