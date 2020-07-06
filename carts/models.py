# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from products.models import product

# Create your models here.

class Cart(models.Model):
	sessionid=models.CharField(max_length=250)
	product_id=models.ForeignKey(product)
	quantity=models.IntegerField()

