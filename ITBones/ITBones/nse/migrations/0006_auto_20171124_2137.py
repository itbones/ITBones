# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nse', '0005_auto_20171124_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nse_m_stocklist',
            name='selldate',
            field=models.DateField(null=True),
        ),
    ]