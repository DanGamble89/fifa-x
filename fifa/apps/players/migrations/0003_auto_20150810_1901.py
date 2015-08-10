# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20150810_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='slug',
            field=models.SlugField(null=True, unique=True, blank=True),
        ),
    ]
