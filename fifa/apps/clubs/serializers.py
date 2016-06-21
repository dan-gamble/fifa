from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from fifa.apps.leagues.serializers import LeagueSerializer
from .models import Club


class ClubSerializer(HyperlinkedModelSerializer):
    league = LeagueSerializer()

    class Meta:
        model = Club
        exclude = ('created', 'modified')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
