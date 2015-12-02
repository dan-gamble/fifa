from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Nation
from .serializers import NationSerializer


class NationViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Nation.objects.all()
    serializer_class = NationSerializer


class NationList(ListView):
    model = Nation
    paginate_by = 25


class NationDetail(DetailView):
    model = Nation
