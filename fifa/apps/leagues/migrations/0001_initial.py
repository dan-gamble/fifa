# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0002_nation_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ea_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('name_abbr', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('nation', models.ForeignKey(null=True, blank=True, to='nations.Nation')),
            ],
            options={
                'verbose_name_plural': 'Leagues',
                'verbose_name': 'League',
            },
        ),
    ]
