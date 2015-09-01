import json
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.http import HttpResponse
from django.utils.text import slugify
from django.views.generic import DetailView, View

from .players.models import Player, PLAYER_HELPERS, PLAYER_POSITION_LINE_CHOICES
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

        # Creates club=club, league=league, etc.
        filters = {model_name.lower(): obj}

        # Grab all of the things we want to filter the players by
        get_filters = self.request.GET.dict()

        # Remove the page key as that is for pagination
        get_filters.pop('page', '')

        position_group = get_filters.pop('group', '')

        if position_group:
            get_filters['position__in'] = position_group.upper().split('-')

        # These are for ordering by, not filtering
        sort_by = get_filters.pop('sort', '')
        sort_order = get_filters.pop('order', '')

        # Get our initial lot of players
        players = Player.objects.filter(
            **filters
        ).select_related(
            'club', 'league', 'nation'
        )

        if sort_by:
            players = players.order_by(
                '{}{}'.format('-' if sort_order == 'desc' else '', sort_by)
            )

        # Grab the form so we can get the fields we filter by
        player_filter_form = PlayersFilterForm()

        # Some of the keys are wrong 'sho_han' for example, need to get the model field name
        sort_filters = {slugify(field.label).replace('-', '_'): field.label for
                        field in player_filter_form}

        # Filter even further based on the GET parameters
        players = players.filter(
            **get_filters
        )

        # Rename to key so it can be removed form the url in the template
        if position_group:
            get_filters['group'] = get_filters.pop('position__in')

        context.update({
            'players': self.pagination(players),
            'player_instance': PLAYER_HELPERS,
            'sort_filters': sort_filters,
            'url_namespace': '{}:{}'.format(
                '{}s'.format(model_name),
                model_name
            ).lower(),
            'get_filters': get_filters
        })

        return context


def card_class(obj):
    card_class = ''
    color_classes = {
        ' is-bronze': ['bronze', 'rare_bronze', 'totw_bronze', 'tots_bronze'],
        ' is-silver': ['silver', 'rare_silver', 'totw_silver', 'tots_silver'],
        ' is-gold': ['gold', 'rare_gold', 'totw_gold', 'tots_gold'],
        ' is-rare': ['rare_bronze', 'rare_silver', 'rare_gold'],
        ' is-totw': ['totw_bronze', 'totw_silver', 'totw_gold'],
        ' is-tots': ['tots_bronze', 'tots_silver', 'tots_gold'],
        ' is-toty': 'toty',
        ' is-motm': 'motm',
        ' is-easports': 'easports',
        ' is-purple': 'purple',
        ' is-green': 'green',
        ' is-pink': 'pink',
        ' is-legend': 'legend'
    }

    print(obj.get('color'))

    for css_class, color in color_classes.items():
        if obj.get('color') in color:
            card_class += css_class

    return card_class.lstrip()


class PlayerJSONList(View):
    def get(self, *args, **kwargs):
        players = serializers.serialize('json', Player.objects.all()[:28])

        return HttpResponse(json.dumps(players))

    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')

        player_list = Player.objects.filter(
            Q(first_name__icontains=text) | Q(last_name__icontains=text)
        ).values(
            'pk', 'common_name', 'color', 'overall_rating', 'image_medium',
            'club__image_medium', 'nation__image_medium', 'slug'
        )[:20]

        players = []

        for player in player_list:
            new_player = {key: value for key, value in player.items()}
            new_player['css_class'] = Player.card_class(player)
            players.append(new_player)

        return HttpResponse(json.dumps(list(players), cls=DjangoJSONEncoder))
