from django.conf.urls import url

from .views import PlayerList, PlayerDetail

urlpatterns = [
    url(r'^$', PlayerList.as_view(), name='players'),
    url(r'^(?P<slug>[\w-]+)/$', PlayerDetail.as_view(), name='player')
]
