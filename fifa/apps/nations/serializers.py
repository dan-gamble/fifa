from rest_framework import serializers
from .models import Nation


class NationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nation
        fields = ('name', 'name_abbr', 'slug', 'image', 'image_sm', 'image_md',
                  'image_lg')
