from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = [
    url(
        r'^$',
        TemplateView.as_view(template_name='base.html'),
        name='homepage'
    ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nations/', include('fifa.apps.nations.urls', namespace='nations')),
]

if settings.DEBUG:
    urlpatterns += [
        url("^404/$", TemplateView.as_view(template_name="404.html")),
        url("^500/$", TemplateView.as_view(template_name="500.html"))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
