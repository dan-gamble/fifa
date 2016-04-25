from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from fifa.apps.builder.views import SquadViewSet
from fifa.apps.nations.views import NationViewSet
from fifa.apps.leagues.views import LeagueViewSet
from fifa.apps.clubs.views import ClubViewSet
from fifa.apps.players.views import PlayerViewSet

admin.autodiscover()

router = DefaultRouter()
router.register(r'squads', SquadViewSet)
router.register(r'nations', NationViewSet)
router.register(r'leagues', LeagueViewSet)
router.register(r'clubs', ClubViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^builder/', include('fifa.apps.builder.urls', namespace='builder')),
    url(r'^nations/', include('fifa.apps.nations.urls', namespace='nations')),
    url(r'^leagues/', include('fifa.apps.leagues.urls', namespace='leagues')),
    url(r'^clubs/', include('fifa.apps.clubs.urls', namespace='clubs')),
    url(r'^players/', include('fifa.apps.players.urls', namespace='players')),

    # Homepage
    url(r'^', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += [
        url("^404/$", TemplateView.as_view(template_name="404.html")),
        url("^500/$", TemplateView.as_view(template_name="500.html"))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
