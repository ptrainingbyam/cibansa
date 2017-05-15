# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 11:14
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20170513_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbtag',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, default=None, editable=False, max_length=200, null=True, populate_from='name'),
        ),
    ]
