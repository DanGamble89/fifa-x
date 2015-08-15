# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='player_average_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='player_count',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='player_count_bronze',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='player_count_gold',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='player_count_silver',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='player_count_special',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
