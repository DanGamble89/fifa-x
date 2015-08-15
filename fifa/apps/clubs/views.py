from django.views.generic import ListView

from .models import Club
from ..views import ObjectDetailView


class ClubList(ListView):
    model = Club
    paginate_by = 50


class ClubDetail(ObjectDetailView):
    model = Club
