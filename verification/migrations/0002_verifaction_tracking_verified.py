# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-23 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='verifaction_tracking',
            name='verified',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]