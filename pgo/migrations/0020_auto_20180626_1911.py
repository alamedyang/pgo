# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-26 19:11
from __future__ import unicode_literals

from django.db import migrations, models


def add_friendship_levels(apps, schema_editor):
    Friendship = apps.get_model('pgo', 'Friendship')
    friendship_data = [
        ('No friend', 1.00),
        ('Good', 1.03),
        ('Great', 1.05),
        ('Ultra', 1.07),
        ('Best', 1.10),
    ]
    for item in friendship_data:
        Friendship.objects.get_or_create(level=item[0], damage_boost=item[1])


class Migration(migrations.Migration):

    dependencies = [
        ('pgo', '0019_pokemon_implemented'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=9)),
                ('damage_boost', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
            options={
                'verbose_name': 'Friendship',
                'verbose_name_plural': 'Friendship',
                'ordering': ('damage_boost',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('level', 'damage_boost')]),
        ),
        migrations.RunPython(add_friendship_levels, migrations.RunPython.noop)
    ]
