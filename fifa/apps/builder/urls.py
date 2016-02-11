from django.conf.urls import url

from .views import SquadList, SquadDetail, BuilderView

urlpatterns = [
    url(r'^$', BuilderView.as_view(), name='builder'),
    url(r'^squads/$', SquadList.as_view(), name='squads'),
    url(r'^(?P<slug>[\w-]+)/$', SquadDetail.as_view(), name='squad')
]
