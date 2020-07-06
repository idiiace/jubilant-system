# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class location(models.Model):
	user=models.ForeignKey(User)
	current_address=models.CharField(max_length=100)
	