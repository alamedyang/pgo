# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-14 20:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pgo', '0010_auto_20171023_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('name', models.CharField(max_length=50, null=True)),
                ('types_boosted', models.ManyToManyField(to='pgo.Type', verbose_name='Boosts Type')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('slug',),
                'verbose_name': 'Weather Condition',
                'verbose_name_plural': 'Weather Conditions',
            },
        ),
    ]