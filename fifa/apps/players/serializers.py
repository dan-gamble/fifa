from rest_framework import serializers

from fifa.apps.clubs.serializers import ClubSerializer
from fifa.apps.leagues.serializers import LeagueSerializer
from fifa.apps.nations.serializers import NationSerializer
from .models import Player


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    club = ClubSerializer()
    league = LeagueSerializer()
    nation = NationSerializer()

    class Meta:
        model = Player
        exclude = ('created', 'modified')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

