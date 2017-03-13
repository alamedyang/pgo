# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-13 22:56
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CPM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.DecimalField(decimal_places=1, max_digits=3)),
                ('value', models.DecimalField(decimal_places=9, max_digits=10)),
            ],
            options={
                'ordering': ('level',),
                'verbose_name': 'CP multiplier',
                'verbose_name_plural': 'CP multiplier',
            },
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('name', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(choices=[('QK', 'Quick'), ('CC', 'Cinematic')], max_length=2)),
                ('legacy', models.BooleanField(default=False)),
                ('power', models.IntegerField(blank=True, default=0)),
                ('energy_delta', models.IntegerField(blank=True, default=0)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('damage_window_start', models.IntegerField(blank=True, null=True)),
                ('damage_window_end', models.IntegerField(blank=True, null=True)),
                ('DPS', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('EPS', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
            ],
            options={
                'ordering': ('-category', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('name', models.CharField(max_length=50, null=True)),
                ('number', models.CharField(max_length=5)),
                ('pgo_attack', models.IntegerField(blank=True, null=True, verbose_name='PGo Attack')),
                ('pgo_defense', models.IntegerField(blank=True, null=True, verbose_name='PGo Defense')),
                ('pgo_stamina', models.IntegerField(blank=True, null=True, verbose_name='PGo Stamina')),
                ('maximum_cp', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Combat Power')),
                ('attack', models.IntegerField(blank=True, null=True)),
                ('special_attack', models.IntegerField(blank=True, null=True)),
                ('defense', models.IntegerField(blank=True, null=True)),
                ('special_defense', models.IntegerField(blank=True, null=True)),
                ('stamina', models.IntegerField(blank=True, null=True)),
                ('speed', models.IntegerField(blank=True, null=True)),
                ('cinematic_moves', models.ManyToManyField(blank=True, related_name='cinematic', to='pgo.Move')),
            ],
            options={
                'ordering': ('number',),
                'verbose_name': 'Pokemon',
                'verbose_name_plural': 'Pokemon',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('name', models.CharField(max_length=50, null=True)),
                ('order', models.PositiveIntegerField(blank=True, null=True)),
                ('strong', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('feeble', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('resistant', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('weak', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='TypeEffectivness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TypeEffectivnessScalar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('name', models.CharField(max_length=50, null=True)),
                ('scalar', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='typeeffectivness',
            name='effectivness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgo.TypeEffectivnessScalar'),
        ),
        migrations.AddField(
            model_name='typeeffectivness',
            name='type_defense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_defense', to='pgo.Type'),
        ),
        migrations.AddField(
            model_name='typeeffectivness',
            name='type_offense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_offense', to='pgo.Type'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='primary_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_types', to='pgo.Type'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='quick_moves',
            field=models.ManyToManyField(blank=True, related_name='quick', to='pgo.Move'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='secondary_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_types', to='pgo.Type'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='move',
            name='move_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pgo.Type'),
        ),
        migrations.AddField(
            model_name='move',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
