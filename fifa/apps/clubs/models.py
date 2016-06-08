from django.core import urlresolvers
from django.db import models
from django.template.defaultfilters import safe

from fifa.apps.models import EaAsset, TimeStampedModel
from fifa.apps.players.models import Player
from ..leagues.models import League


class Club(EaAsset, TimeStampedModel, models.Model):
    cached_url = models.CharField(max_length=1000, null=True, blank=True)

    name = models.CharField(max_length=100)
    name_abbr = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    league = models.ForeignKey(League, blank=True, null=True)

    image_dark_sm = models.CharField(max_length=255, blank=True, null=True)
    image_dark_md = models.CharField(max_length=255, blank=True, null=True)
    image_dark_lg = models.CharField(max_length=255, blank=True, null=True)

    image_normal_sm = models.CharField(max_length=255, blank=True, null=True)
    image_normal_md = models.CharField(max_length=255, blank=True, null=True)
    image_normal_lg = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    def __str__(self):
        return self.name

    def get_absolute_url(self, cached=False):
        if self.cached_url and cached:
            return self.cached_url

        url = urlresolvers.reverse('clubs:club', kwargs={'slug': self.slug})

        if url != self.cached_url:
            self.cached_url = url
            self.save()

        return url

    def related_object(self):
        return self.league

    def detail_title(self):
        split = self.name.split(' ')
        last_item = split.pop()
        split.append('<span class="hlt-Red">{}</span>'.format(last_item))

        return safe(' '.join(split))


