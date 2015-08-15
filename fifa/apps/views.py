from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView

from .players.models import Player


class ObjectDetailView(DetailView):
    template_name = 'shared/detail.html'

    def pagination(self, queryset, page_count=28):
        # Create pagination for the players return
        paginator = Paginator(queryset, page_count)

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

        return pagination

    def get_context_data(self, **kwargs):
        context = super(ObjectDetailView, self).get_context_data()

        obj = self.get_object()
        model_name = type(obj).__name__

        filters = {model_name.lower(): obj}

        players = Player.objects.filter(
            **filters
        ).select_related(
            'club', 'league', 'nation'
        )

        players = players.filter(
            **self.request.GET.dict()
        )

        context['levels'] = Player.player_levels()

        context['players'] = self.pagination(players)

        return context
