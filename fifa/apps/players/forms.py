from django import forms

from .models import Player


class PlayersFilterForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ['name', 'first_name', 'last_name', 'common_name', 'slug',
                   'order', 'image_small', 'image_medium', 'image_large',
                   'position_full', 'ea_id_unique', 'play_style', 'item_type',
                   'ea_id', 'created', 'modified', 'is_fut_player']

    def __init__(self, *args, **kwargs):
        super(PlayersFilterForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            self.fields[key].required = False
