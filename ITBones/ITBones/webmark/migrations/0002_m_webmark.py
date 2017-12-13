# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmark', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='m_webmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.CharField(max_length=30)),
                ('topic', models.CharField(max_length=100)),
                ('addinfo', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=150)),
                ('linkinfo', models.TextField()),
                ('user', models.CharField(max_length=50)),
                ('stamp', models.DateTimeField()),
            ],
        ),
    ]
