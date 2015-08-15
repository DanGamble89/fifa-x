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

        self.fields['card_att_1'].label = 'PAC / DIV'
        self.fields['card_att_2'].label = 'SHO / HAN'
        self.fields['card_att_3'].label = 'PAS / KIC'
        self.fields['card_att_4'].label = 'DRI / REF'
        self.fields['card_att_5'].label = 'DEF / SPE'
        self.fields['card_att_6'].label = 'PHY / POS'

        for key, field in self.fields.items():
            self.fields[key].required = False
