# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-06 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=200)),
                ('hits', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Stat',
                'verbose_name_plural': 'Stats',
            },
        ),
    ]
