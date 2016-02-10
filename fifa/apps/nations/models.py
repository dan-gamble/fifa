from django.db import models
from django.utils.text import slugify

from fifa.apps.models import EaAsset, TimeStampedModel


class Nation(EaAsset, TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    name_abbr = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    image = models.CharField(max_length=255, blank=True, null=True)

    image_sm = models.CharField(max_length=255, blank=True, null=True)
    image_md = models.CharField(max_length=255, blank=True, null=True)
    image_lg = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Nation'
        verbose_name_plural = 'Nations'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)

        super(Nation, self).save()
