# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-23 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_recommended_topitems'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recommended',
            options={'verbose_name_plural': 'recommended'},
        ),
        migrations.AlterModelOptions(
            name='topitems',
            options={'verbose_name_plural': 'topitems'},
        ),
    ]
