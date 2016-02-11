from rest_framework import serializers
from .models import Nation


class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation
        exclude = ('created', 'modified')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
