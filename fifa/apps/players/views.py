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
            for item in remove:
                params.pop(item, None)

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

    def get_queryset(self):
        return super(PlayerDetail, self).get_queryset().select_related(
            'club', 'league', 'nation'
        )

    def get_context_data(self, **kwargs):
        context = super(PlayerDetail, self).get_context_data()

        print(Player.objects.filter(acceleration__lt=self.get_object().acceleration).count())
        print(Player.objects.filter(acceleration__lt=self.get_object().acceleration).count())
        print(Player.objects.filter(aggression__lt=self.get_object().aggression).count())
        print(Player.objects.filter(agility__lt=self.get_object().agility).count())
        print(Player.objects.filter(balance__lt=self.get_object().balance).count())
        print(Player.objects.filter(ball_control__lt=self.get_object().ball_control).count())
        print(Player.objects.filter(skill__lt=self.get_object().skill).count())
        print(Player.objects.filter(weak_foot__lt=self.get_object().weak_foot).count())
        print(Player.objects.filter(crossing__lt=self.get_object().crossing).count())
        print(Player.objects.filter(curve__lt=self.get_object().curve).count())
        print(Player.objects.filter(dribbling__lt=self.get_object().dribbling).count())
        print(Player.objects.filter(finishing__lt=self.get_object().finishing).count())
        print(Player.objects.filter(free_kick_accuracy__lt=self.get_object().free_kick_accuracy).count())
        print(Player.objects.filter(gk_diving__lt=self.get_object().gk_diving).count())
        print(Player.objects.filter(gk_handling__lt=self.get_object().gk_handling).count())
        print(Player.objects.filter(gk_kicking__lt=self.get_object().gk_kicking).count())
        print(Player.objects.filter(gk_positioning__lt=self.get_object().gk_positioning).count())
        print(Player.objects.filter(gk_reflex__lt=self.get_object().gk_reflex).count())
        print(Player.objects.filter(heading_accuracy__lt=self.get_object().heading_accuracy).count())
        print(Player.objects.filter(interceptions__lt=self.get_object().interceptions).count())
        print(Player.objects.filter(jumping__lt=self.get_object().jumping).count())
        print(Player.objects.filter(long_passing__lt=self.get_object().long_passing).count())
        print(Player.objects.filter(long_shots__lt=self.get_object().long_shots).count())
        print(Player.objects.filter(marking__lt=self.get_object().marking).count())
        print(Player.objects.filter(penalties__lt=self.get_object().penalties).count())
        print(Player.objects.filter(positioning__lt=self.get_object().positioning).count())
        print(Player.objects.filter(potential__lt=self.get_object().potential).count())
        print(Player.objects.filter(reactions__lt=self.get_object().reactions).count())
        print(Player.objects.filter(short_passing__lt=self.get_object().short_passing).count())
        print(Player.objects.filter(shot_power__lt=self.get_object().shot_power).count())
        print(Player.objects.filter(sliding_tackle__lt=self.get_object().sliding_tackle).count())
        print(Player.objects.filter(sprint_speed__lt=self.get_object().sprint_speed).count())
        print(Player.objects.filter(standing_tackle__lt=self.get_object().standing_tackle).count())
        print(Player.objects.filter(stamina__lt=self.get_object().stamina).count())
        print(Player.objects.filter(strength__lt=self.get_object().strength).count())
        print(Player.objects.filter(vision__lt=self.get_object().vision).count())
        print(Player.objects.filter(volleys__lt=self.get_object().volleys).count())

        return context
