# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_auto_20150815_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='card_att_1_label',
        ),
        migrations.RemoveField(
            model_name='player',
            name='card_att_2_label',
        ),
        migrations.RemoveField(
            model_name='player',
            name='card_att_3_label',
        ),
        migrations.RemoveField(
            model_name='player',
            name='card_att_4_label',
        ),
        migrations.RemoveField(
            model_name='player',
            name='card_att_5_label',
        ),
        migrations.RemoveField(
            model_name='player',
            name='card_att_6_label',
        ),
    ]
