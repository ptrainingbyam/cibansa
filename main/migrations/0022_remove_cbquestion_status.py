# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-14 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20170613_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cbquestion',
            name='status',
        ),
    ]
