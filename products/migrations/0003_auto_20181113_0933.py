# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181113_0931'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
        
    ]
