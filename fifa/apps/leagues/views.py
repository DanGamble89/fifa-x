from django.views.generic import ListView
from fifa.apps.players.models import Player

from .models import League
from ..views import ObjectDetailView


class LeagueList(ListView):
    model = League
    paginate_by = 50


class LeagueDetail(ObjectDetailView):
    model = League

    def get_context_data(self, **kwargs):
        context = super(LeagueDetail, self).get_context_data()

        players = Player.objects.filter(
            league=self.get_object()
        ).select_related(
            'club', 'league', 'nation'
        )

        context['players'] = self.pagination(players)

        return context
