# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 21:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0004_auto_20151130_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('formation', models.CharField(choices=[('3412', '3-4-1-2'), ('3421', '3-4-2-1'), ('343', '3-4-3'), ('352', '3-5-2'), ('41212', '4-1-2-1-2'), ('41212-2', '4-1-2-1-2 (2)'), ('4141', '4-1-4-1'), ('4231', '4-2-3-1'), ('4231-2', '4-2-3-1 (2)'), ('4222', '4-2-2-2'), ('4312', '4-3-1-2'), ('4321', '4-3-2-1'), ('433', '4-3-3'), ('433-2', '4-3-3 (2)'), ('433-3', '4-3-3 (3)'), ('433-4', '4-3-3 (4)'), ('433-5', '4-3-3 (5)'), ('4411', '4-4-1-1'), ('442', '4-4-2'), ('442-2', '4-4-2 (2)'), ('451', '4-5-1'), ('451-2', '4-5-1 (2)'), ('5212', '5-2-1-2'), ('5221', '5-2-2-1'), ('532', '5-3-2')], max_length=10)),
                ('chemistry', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('attack', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('midfield', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('defence', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('pace', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('shooting', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('passing', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('dribbling', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('defending', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('physical', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SquadLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=3)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player')),
                ('squad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.Squad')),
            ],
        ),
        migrations.AddField(
            model_name='squad',
            name='players',
            field=models.ManyToManyField(through='builder.SquadLocation', to='players.Player'),
        ),
    ]