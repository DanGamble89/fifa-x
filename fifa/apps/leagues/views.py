from django.db.models.loading import get_model
from django.views.generic import ListView
from fifa.apps.players.models import Player

from .models import League
from ..views import ObjectDetailView


class LeagueList(ListView):
    model = League
    paginate_by = 50


class LeagueDetail(ObjectDetailView):
    model = League
