from django.views.generic import ListView, DetailView

from .models import Nation


class NationList(ListView):
    model = Nation
    paginate_by = 50


class NationDetail(DetailView):
    model = Nation
