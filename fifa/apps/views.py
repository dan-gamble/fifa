from django.views.generic import DetailView

from fifa.apps.players.models import Player


class EaDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        qs = {
            self.model._meta.model_name: self.get_object()
        }

        context['players'] = Player.objects.filter(**qs)

        return context
