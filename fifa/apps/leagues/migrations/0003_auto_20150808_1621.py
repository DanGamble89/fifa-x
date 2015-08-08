# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_auto_20150804_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='nation',
            field=models.ForeignKey(blank=True, to='nations.Nation', null=True),
        ),
    ]
