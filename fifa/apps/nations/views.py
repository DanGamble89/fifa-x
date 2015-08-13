from django.views.generic import ListView
from fifa.apps.players.models import Player

from .models import Nation
from ..views import ObjectDetailView


class NationList(ListView):
    model = Nation
    paginate_by = 50


class NationDetail(ObjectDetailView):
    model = Nation
