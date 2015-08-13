from django.views.generic import ListView
from fifa.apps.players.models import Player

from .models import Nation
from ..views import ObjectDetailView


class NationList(ListView):
    model = Nation
    paginate_by = 50


class NationDetail(ObjectDetailView):
    model = Nation

    def get_context_data(self, **kwargs):
        context = super(NationDetail, self).get_context_data()

        players = Player.objects.filter(
            nation=self.get_object()
        ).select_related(
            'club', 'league', 'nation'
        )

        context['players'] = self.pagination(players)

        return context
