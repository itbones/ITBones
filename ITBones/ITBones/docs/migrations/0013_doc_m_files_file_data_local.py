# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-22 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0012_auto_20171219_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc_m_files',
            name='file_data_local',
            field=models.FileField(blank=True, upload_to='Documents'),
        ),
    ]