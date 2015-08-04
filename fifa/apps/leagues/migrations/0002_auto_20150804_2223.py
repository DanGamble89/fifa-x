# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='image_dark_large',
        ),
        migrations.RemoveField(
            model_name='league',
            name='image_dark_small',
        ),
        migrations.RemoveField(
            model_name='league',
            name='image_light_large',
        ),
        migrations.RemoveField(
            model_name='league',
            name='image_light_small',
        ),
    ]
