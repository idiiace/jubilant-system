# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181117_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]
