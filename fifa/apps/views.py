from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.text import slugify
from django.views.generic import DetailView

from .players.models import Player, PLAYER_HELPERS
from .players.forms import PlayersFilterForm


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
        player_filter_form = PlayersFilterForm()
        # Some of the keys are wrong 'sho_han' for example, need to get the model field name
        sort_filters = {slugify(field.label).replace('-', '_'): field.label for field in player_filter_form}

        print(sort_filters)

        get_filters = self.request.GET.dict()
        sort_by = get_filters.pop('sort', '')
        sort_order = get_filters.pop('order', '')

        filters = {model_name.lower(): obj}

        players = Player.objects.filter(
            **filters
        ).select_related(
            'club', 'league', 'nation'
        ).order_by(
            '{}{}'.format('-' if sort_order == 'desc' else '', sort_by)
        )

        players = players.filter(
            **get_filters
        )

        context.update({
            'players': self.pagination(players),
            'player_instance': PLAYER_HELPERS,
            'sort_filters': sort_filters
        })

        return context
