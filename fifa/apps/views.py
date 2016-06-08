from django.views.generic import DetailView

from fifa.apps.players.models import Player


class EaDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_object = self.get_object().related_object()

        players_filter = {
            self.model._meta.model_name: self.get_object()
        }

        context['players'] = Player.objects.filter(**players_filter)

        if related_object:
            related_objects_filter = {
                'club': {
                    related_object._meta.model_name: related_object
                },
                'league': {},
                'nation': None
            }

            context['related_objects'] = self.model.objects.filter(
                **related_objects_filter[self.model._meta.model_name]
            )

        return context
