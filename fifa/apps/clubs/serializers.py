from rest_framework import serializers

from fifa.apps.leagues.serializers import LeagueSerializer
from .models import Club


class ClubSerializer(serializers.ModelSerializer):
    league = LeagueSerializer()

    class Meta:
        model = Club
        exclude = ('created', 'modified')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
