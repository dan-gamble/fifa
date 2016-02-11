from rest_framework import serializers

from fifa.apps.players.serializers import PlayerSerializer
from .models import Squad


class SquadSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Squad
        exclude = ('created', 'modified')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
