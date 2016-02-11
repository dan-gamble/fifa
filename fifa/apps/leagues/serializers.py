from rest_framework import serializers

from fifa.apps.nations.serializers import NationSerializer
from .models import League


class LeagueSerializer(serializers.ModelSerializer):
    nation = NationSerializer()

    class Meta:
        model = League
        exclude = ('created', 'modified')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
