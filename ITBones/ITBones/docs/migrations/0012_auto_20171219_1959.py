# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-19 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0011_auto_20171216_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc_m_files',
            name='file_gname',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='doc_m_files',
            name='file_url',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='doc_m_files',
            name='file_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]