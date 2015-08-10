# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='specialities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True, blank=True, max_length=255), null=True, blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='player',
            name='traits',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True, blank=True, max_length=255), null=True, blank=True, size=None),
        ),
    ]
