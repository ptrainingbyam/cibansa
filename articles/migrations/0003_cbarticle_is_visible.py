# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20170523_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbarticle',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
