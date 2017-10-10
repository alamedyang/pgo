# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-10 19:50
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('name', models.CharField(max_length=50, null=True)),
                ('trainer_count', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('name', models.CharField(max_length=50, null=True)),
                ('trainer_count', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(choices=[('yellow', 'Yellow'), ('blue', 'Blue'), ('red', 'Red'), ('green', 'Green')], default='yellow', max_length=10)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('name', models.CharField(max_length=50, null=True)),
                ('trainer_count', models.PositiveIntegerField(default=0)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registry.Country')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('nickname', models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]{4,}$', 'Nicknames are 4-15 characters long and consist only of letters and numbers.')])),
                ('level', models.PositiveIntegerField(blank=True, help_text='Level 20 is the minimum level required to be included in the registry.', null=True, validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(40)])),
                ('legit', models.BooleanField(default=True, help_text='Will never be shown publicly, untick only for confirmed spoofers/botters.')),
                ('recruited', models.BooleanField(default=False, help_text='The trainer is included in our groups/chats.')),
                ('retired', models.BooleanField(default=False, help_text='The trainer used to play, but they no longer do, or at least not currently.')),
                ('team', models.ForeignKey(help_text='Select "Harmony" if the trainer has never chosen a team.', on_delete=django.db.models.deletion.CASCADE, to='registry.Team')),
                ('towns', models.ManyToManyField(blank=True, help_text='Where the trainer usually plays.', related_name='trainers', to='registry.Town')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
