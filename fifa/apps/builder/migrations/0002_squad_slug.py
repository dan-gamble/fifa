# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
