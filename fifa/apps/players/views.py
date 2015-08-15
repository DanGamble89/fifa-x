from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, BaseFormView

from .forms import PlayersFilterForm
from .models import Player

import urllib.parse


def build_url(*args, **kwargs):
    request = kwargs.pop('request', {})
    get = kwargs.pop('get', {})
    remove = kwargs.pop('remove', '')
    url = ''

    # Sometimes no 'viewname' is passed i.e. building pagination links
    if args or kwargs:
        url = reverse(*args, **kwargs)

    if hasattr(request, 'dict'):
        params = request.dict()

        if remove:
            params.pop(remove, None)

        # get_key = ''.join(['{}'.format(k) for k, v in get.items()])
        # get_value = ''.join(['{}'.format(v) for k, v in get.items()])
        #
        # if get_key in params and params[get_key] == get_value:
        #     pass
        # else:
        params.update(**get)

        url += '?{}'.format(urllib.parse.urlencode(params))

    return url


class PlayerList(ListView, FormMixin):
    context_object_name = 'players'
    form_class = PlayersFilterForm
    model = Player
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super(PlayerList, self).get_context_data()

        if self.request.GET:
            context['form'] = PlayersFilterForm(self.request.GET)
        else:
            context['form'] = PlayersFilterForm()

        context['current_url'] = self.request.get_full_path()

        return context

    def get_queryset(self, **kwargs):
        qs = super(PlayerList, self).get_queryset().prefetch_related(
            'club',
            'league',
            'nation'
        )

        arguments = {}

        for k, v in self.request.GET.dict().items():
            if k == 'csrfmiddlewaretoken':
                pass
            elif v:
                arguments[k] = v

        qs = qs.filter(
            **arguments
        )

        return qs


class PlayerDetail(DetailView):
    model = Player
