from django.db import models

from fifa.apps.models import EaAsset, TimeStampedModel
from ..nations.models import Nation


class League(EaAsset, TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    name_abbr = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    nation = models.ForeignKey(Nation, blank=True, null=True)

    class Meta:
        verbose_name = 'League'
        verbose_name_plural = 'Leagues'

    def __str__(self):
        return self.name
