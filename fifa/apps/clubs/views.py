from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .models import Club
from .serializers import ClubSerializer


class ClubViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class ClubList(ListView):
    model = Club
    paginate_by = 25


class ClubDetail(DetailView):
    model = Club
