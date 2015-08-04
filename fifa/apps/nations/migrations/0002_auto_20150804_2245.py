# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nation',
            name='image_large',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='nation',
            name='image_medium',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='nation',
            name='image_small',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
