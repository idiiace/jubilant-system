# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0002_delete_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_address', models.CharField(max_length=100)),
            ],
        ),
    ]
