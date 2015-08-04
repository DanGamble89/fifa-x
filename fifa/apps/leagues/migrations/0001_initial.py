# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ea_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('name_abbr', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image_medium', models.CharField(max_length=500)),
                ('image_dark_small', models.CharField(max_length=500)),
                ('image_dark_large', models.CharField(max_length=500)),
                ('image_light_small', models.CharField(max_length=500)),
                ('image_light_large', models.CharField(max_length=500)),
                ('order', models.PositiveIntegerField(default=0)),
                ('nation', models.ForeignKey(to='nations.Nation')),
            ],
            options={
                'verbose_name_plural': 'Leagues',
                'verbose_name': 'League',
                'ordering': ('order', 'name', 'pk'),
            },
        ),
    ]
