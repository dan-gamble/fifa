# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20151130_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['-overall_rating', '-ea_id'], 'verbose_name': 'Player', 'verbose_name_plural': 'Players'},
        ),
        migrations.AddField(
            model_name='player',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
