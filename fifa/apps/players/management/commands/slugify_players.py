from django.core.management import BaseCommand
from django.utils.text import slugify

from ...models import Player


class Command(BaseCommand):
    def handle(self, *args, **options):
        players = Player.objects.all()

        for player in players:
            player.slug = slugify('{}-{}'.format(player.pk, player.common_name))
            print(player.slug)
            player.save()
