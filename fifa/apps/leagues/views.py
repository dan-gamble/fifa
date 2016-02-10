from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .models import League
from .serializers import LeagueSerializer


class LeagueViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class LeagueList(ListView):
    model = League
    paginate_by = 25


class LeagueDetail(DetailView):
    model = League
