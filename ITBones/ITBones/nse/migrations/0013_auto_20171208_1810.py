# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nse', '0012_auto_20171208_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nse_m_stocknews',
            name='notedate',
            field=models.DateField(null=True),
        ),
    ]
