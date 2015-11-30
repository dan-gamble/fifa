# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nation',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
