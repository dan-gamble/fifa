import json

from django.views.generic import ListView, DetailView, TemplateView
from rest_framework import viewsets

from .models import Squad, FORMATION_CHOICES
from .serializers import SquadSerializer


class SquadViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer


class BuilderView(TemplateView):
    template_name = 'builder/builder.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formations'] = json.dumps(
            dict(map(reversed, FORMATION_CHOICES))
        )

        return context


class SquadList(ListView):
    model = Squad
    paginate_by = 25


class SquadDetail(DetailView):
    model = Squad

