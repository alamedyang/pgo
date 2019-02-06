# Generated by Django 2.1.5 on 2019-02-05 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgo', '0018_auto_20190205_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moveavailability',
            name='legacy_status',
            field=models.CharField(choices=[('CD', 'Community day'), ('RD', 'Raid day'), ('QE', 'Quest encounter'), ('RM', 'Removed'), ('AC', 'Active')], default='AC', max_length=2),
        ),
    ]
