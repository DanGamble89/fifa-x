# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20150815_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='acceleration',
            field=models.PositiveIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='position_line',
            field=models.CharField(max_length=3, choices=[('GK', 'Goalkeepers'), ('DEF', 'Defenders'), ('MID', 'Midfielders'), ('ATT', 'Attackers')]),
        ),
    ]
