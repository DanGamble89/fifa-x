# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0003_auto_20150808_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ea_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('name_abbr', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image_dark_small', models.CharField(max_length=500, blank=True)),
                ('image_dark_large', models.CharField(max_length=500, blank=True)),
                ('image_light_small', models.CharField(max_length=500, blank=True)),
                ('image_light_large', models.CharField(max_length=500, blank=True)),
                ('image_medium', models.CharField(max_length=500)),
                ('order', models.PositiveIntegerField(default=0)),
                ('league', models.ForeignKey(to='leagues.League')),
            ],
            options={
                'verbose_name_plural': 'Clubs',
                'verbose_name': 'Club',
                'ordering': ('order', 'name', 'pk'),
            },
        ),
    ]
