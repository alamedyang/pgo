# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-19 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgo', '0006_auto_20170819_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='raid_stamina',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='raid_tier',
        ),
    ]