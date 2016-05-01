from django.views.generic import ListView
from rest_framework import viewsets

from fifa.apps.views import EaDetailView
from .models import League
from .serializers import LeagueSerializer


class LeagueViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class LeagueList(ListView):
    model = League
    paginate_by = 25

    def get_queryset(self):
        return super(LeagueList, self).get_queryset().select_related('nation')


class LeagueDetail(EaDetailView):
    model = League
