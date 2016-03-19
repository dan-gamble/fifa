from django.db.models import Q
from django.views.generic import ListView, DetailView
from rest_framework import viewsets, filters
from .models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('first_name', 'last_name', 'common_name')

    def get_queryset(self):
        query = self.request.query_params.get('query', None)

        if query:
            qs = Player.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(common_name__icontains=query)
            )
        else:
            qs = Player.objects.all()

        return qs


class PlayerList(ListView):
    model = Player
    paginate_by = 25

    def get_queryset(self):
        return super(PlayerList, self).get_queryset().select_related('club', 'league', 'nation')

    def get_context_data(self, **kwargs):
        context = super(PlayerList, self).get_context_data()

        print(self.request.GET)

        context['current_query'] = self.request.GET.urlencode()

        return context


class PlayerDetail(DetailView):
    model = Player
