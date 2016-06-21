from django.views.generic import ListView
from rest_framework import viewsets, filters
from rest_framework.response import Response

from fifa.apps.views import EaDetailView
from .models import Nation
from .serializers import NationSerializer


class NationViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Nation.objects.all()
    serializer_class = NationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)


class NationList(ListView):
    model = Nation
    paginate_by = 25


class NationDetail(EaDetailView):
    model = Nation
