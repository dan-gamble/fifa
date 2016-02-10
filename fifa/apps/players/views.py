from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerList(ListView):
    model = Player
    paginate_by = 25


class PlayerDetail(DetailView):
    model = Player
