# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20150810_1901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name_plural': 'Players', 'ordering': ('order', '-overall_rating', 'common_name', 'pk'), 'verbose_name': 'Player'},
        ),
    ]
