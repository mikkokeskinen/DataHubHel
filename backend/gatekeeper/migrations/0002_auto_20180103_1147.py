# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gatekeeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datastream',
            options={'permissions': (('subscribe_datastream', 'Can subscribe to the data stream topic'), ('publish_datastream', 'Can publish to the data stream topic')), 'verbose_name': 'data stream', 'verbose_name_plural': 'data streams'},
        ),
    ]
