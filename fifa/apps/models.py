from django.db import models


class EaAsset(models.Model):
    ea_id = models.PositiveIntegerField()

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
