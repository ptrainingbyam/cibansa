# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-31 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_cbquestion_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbcategory',
            name='image',
            field=models.ImageField(default='default_category_img.jpg', upload_to=main.models.category_image_path),
        ),
    ]