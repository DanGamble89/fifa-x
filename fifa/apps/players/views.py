from django.views.generic import ListView, DetailView

from .models import Player


class PlayerList(ListView):
    context_object_name = 'players'
    model = Player
    paginate_by = 50


class PlayerDetail(DetailView):
    model = Player
