# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ea_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('name_abbr', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image_small', models.CharField(max_length=500)),
                ('image_medium', models.CharField(max_length=500)),
                ('image_large', models.CharField(max_length=500)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order', 'name', 'pk'),
                'verbose_name': 'Nation',
                'verbose_name_plural': 'Nations',
            },
        ),
    ]
