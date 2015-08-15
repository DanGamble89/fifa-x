# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0003_auto_20150815_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nation',
            name='player_average_rating',
            field=models.FloatField(null=True),
        ),
    ]
