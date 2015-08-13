from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView
from fifa.apps.players.models import Player

from .models import Nation


class NationList(ListView):
    model = Nation
    paginate_by = 50


class NationDetail(DetailView):
    model = Nation

    def get_context_data(self, **kwargs):
        context = super(NationDetail, self).get_context_data()

        players = Player.objects.filter(
            nation=self.get_object()
        ).select_related(
            'club', 'league'
        )

        # Create pagination for the players return
        paginator = Paginator(players, 28)

        # Get the page from the URL
        page = self.request.GET.get('page')

        try:
            # Deliver the requested page
            pagination = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            pagination = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            pagination = paginator.page(paginator.num_pages)

        context['players'] = pagination

        return context
