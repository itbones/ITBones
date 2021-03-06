# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nse_m_stocklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.CharField(max_length=30)),
                ('stock_desc', models.CharField(max_length=100)),
                ('buyprice', models.CharField(max_length=10)),
                ('buyqty', models.CharField(max_length=10)),
                ('buydate', models.CharField(blank=True, max_length=30)),
                ('notval1', models.CharField(max_length=10)),
                ('notval2', models.CharField(max_length=10)),
                ('notval3', models.CharField(max_length=10)),
                ('buyvalue', models.CharField(blank=True, max_length=10)),
                ('currprice', models.CharField(blank=True, max_length=10)),
                ('currvalue', models.CharField(blank=True, max_length=10)),
                ('realpos', models.CharField(blank=True, max_length=10)),
                ('notes', models.TextField(blank=True)),
                ('stock_type', models.CharField(blank=True, max_length=2)),
                ('selldate', models.CharField(blank=True, max_length=30)),
                ('sellprice', models.CharField(blank=True, max_length=10)),
                ('sellvalue', models.CharField(blank=True, max_length=10)),
                ('plfinal', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
