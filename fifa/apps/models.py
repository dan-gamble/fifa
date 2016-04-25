from django.db import models


class EaAsset(models.Model):
    ea_id = models.PositiveIntegerField()

    class Meta:
        abstract = True

    @staticmethod
    def player_object():
        from fifa.apps.players.models import Player

        return Player

    def model_name(self):
        return self._meta.model_name

    def players(self):
        model_filter = {self.model_name(): self}

        return self.player_object().objects.filter(**model_filter)

    def bronze_players(self):
        return self.players().filter(
            models.Q(color='bronze') | models.Q(color='rare_bronze')
        ).order_by('-color')

    def silver_players(self):
        return self.players().filter(
            models.Q(color='silver') | models.Q(color='rare_silver')
        ).order_by('-color')

    def gold_players(self):
        return self.players().filter(
            models.Q(color='gold') | models.Q(color='rare_gold')
        ).order_by('-color')

    def totw_players(self):
        return self.players().filter(
            models.Q(color='totw_bronze') | models.Q(color='totw_silver') | models.Q(color='totw_gold')
        ).order_by('-color')

    def special_players(self):
        return self.players().filter(is_special_type=True)


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
