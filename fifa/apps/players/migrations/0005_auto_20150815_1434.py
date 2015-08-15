# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20150815_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='card_att_1_label',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='card_att_2_label',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='card_att_3_label',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='card_att_4_label',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='card_att_5_label',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='card_att_6_label',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(max_length=3, choices=[('GK', 'GK'), ('RWB', 'RWB'), ('RB', 'RB'), ('CB', 'CB'), ('LB', 'LB'), ('LWB', 'LWB'), ('CDM', 'CDM'), ('CM', 'CM'), ('CAM', 'CAM'), ('RM', 'RM'), ('RW', 'RW'), ('RF', 'RF'), ('LM', 'LM'), ('LW', 'LW'), ('LF', 'LF'), ('CF', 'CF'), ('ST', 'ST')]),
        ),
        migrations.AlterField(
            model_name='player',
            name='position_line',
            field=models.CharField(max_length=3, choices=[('GK', 'GK'), ('DEF', 'DEF'), ('MID', 'MID'), ('ATT', 'ATT')]),
        ),
    ]
