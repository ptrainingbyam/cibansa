# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 12:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20170505_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbcategory',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_categories', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cbtopic',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_topic', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
