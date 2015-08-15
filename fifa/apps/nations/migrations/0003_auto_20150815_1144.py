# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0002_auto_20150804_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='nation',
            name='player_average_rating',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nation',
            name='player_count',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nation',
            name='player_count_bronze',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nation',
            name='player_count_gold',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nation',
            name='player_count_silver',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nation',
            name='player_count_special',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
