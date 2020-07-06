# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from products.models import *

class order(models.Model):
	products=models.ManyToManyField(product)
	user=models.ForeignKey(User)

