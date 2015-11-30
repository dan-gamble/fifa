from django.db import models

from fifa.apps.models import EaAsset, TimeStampedModel
from ..leagues.models import League


class Club(EaAsset, TimeStampedModel, models.Model):
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
