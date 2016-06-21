from django.db.models import Q
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from rest_framework import viewsets, filters
from .models import Player
from .serializers import PlayerSerializer
from .utils import build_querystring


class PlayerViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('first_name', 'last_name', 'common_name')

    def get_queryset(self):
        query = self.request.query_params.get('query', None)

        qs = Player.objects.all()

        if query:
            qs = qs.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(common_name__icontains=query)
            )

        nation = self.request.query_params.get('nation', None)

        if nation:
            qs = qs.filter(nation__slug=slugify(nation))

        print(query, nation)

        return qs


class PlayerList(ListView):
    model = Player
    paginate_by = 25

    def get_queryset(self):
        qs = super(PlayerList, self).get_queryset().select_related('club', 'league', 'nation')

        qs = qs.filter(**build_querystring(self.request.GET.items()))

        return qs

    def get_context_data(self, **kwargs):
        context = super(PlayerList, self).get_context_data()

        context['skill_moves_options'] = Player.objects\
            .order_by('skill_moves')\
            .values_list('skill_moves', flat=True)\
            .distinct()

        context['weak_foot_options'] = Player.objects\
            .order_by('weak_foot')\
            .values_list('weak_foot', flat=True)\
            .distinct()

        context['att_workrate_options'] = Player.objects\
            .order_by('workrate_att')\
            .values_list('workrate_att', flat=True)\
            .distinct()

        context['def_workrate_options'] = Player.objects\
            .order_by('workrate_def')\
            .values_list('workrate_def', flat=True)\
            .distinct()

        context['strong_foot_options'] = Player.objects\
            .order_by('foot')\
            .values_list('foot', flat=True)\
            .distinct()

        context['position_options'] = Player.objects\
            .order_by('position')\
            .values_list('position', flat=True)\
            .distinct()

        context['age_options'] = Player.objects\
            .order_by('age')\
            .values_list('age', flat=True)\
            .distinct()

        context['type_options'] = Player.objects\
            .order_by('player_type')\
            .values_list('player_type', flat=True)\
            .distinct()

        context['color_options'] = Player.objects\
            .order_by('color')\
            .values_list('color', flat=True)\
            .distinct()

        return context


class PlayerDetail(DetailView):
    model = Player
