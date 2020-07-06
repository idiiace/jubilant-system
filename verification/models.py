# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class verifaction_tracking(models.Model):
	sessionid=models.CharField(max_length=250)
	phonenumber=models.CharField(max_length=250)
	verfication_code=models.IntegerField()
	verified=models.BooleanField()

	def __str__(self):
		return self.phonenumber

class user_is_veried(models.Model):
	username=models.ForeignKey(User)
	is_veried=models.BooleanField()







