# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('ea_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('name_abbr', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image_dark_sm', models.CharField(blank=True, null=True, max_length=255)),
                ('image_dark_md', models.CharField(blank=True, null=True, max_length=255)),
                ('image_dark_lg', models.CharField(blank=True, null=True, max_length=255)),
                ('image_normal_sm', models.CharField(blank=True, null=True, max_length=255)),
                ('image_normal_md', models.CharField(blank=True, null=True, max_length=255)),
                ('image_normal_lg', models.CharField(blank=True, null=True, max_length=255)),
                ('league', models.ForeignKey(blank=True, to='leagues.League', null=True)),
            ],
            options={
                'verbose_name_plural': 'Clubs',
                'verbose_name': 'Club',
            },
        ),
    ]
