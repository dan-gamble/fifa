from django.core import urlresolvers
from django.db import models
from django.template.defaultfilters import safe
from django.utils.text import slugify

from fifa.apps.models import EaAsset, TimeStampedModel


class Nation(EaAsset, TimeStampedModel, models.Model):
    cached_url = models.CharField(max_length=1000, null=True, blank=True)

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

    def get_absolute_url(self, cached=False):
        if self.cached_url and cached:
            return self.cached_url

        url = urlresolvers.reverse('nations:nation', kwargs={'slug': self.slug})

        if url != self.cached_url:
            self.cached_url = url
            self.save()

        return url

    def related_object(self):
        return None

    def detail_title(self):
        split = self.name.split(' ')
        last_item = split.pop()
        split.append('<span class="hlt-Red">{}</span>'.format(last_item))

        return safe(' '.join(split))
