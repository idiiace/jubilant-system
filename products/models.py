# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

class category(models.Model):
	name=models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	parent_id=models.ForeignKey('category',null=True, blank=True,)

	def slug(self):
		return slugify(self.name)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "categories"


class product(models.Model):
	name=models.CharField(max_length=255)
	date=models.DateField()
	image=models.ImageField()
	category=models.ForeignKey('category')
	price=models.IntegerField()
	rating=models.IntegerField()
	skd=models.CharField(max_length=255)
	description=models.CharField(max_length=1000)
	instock=models.IntegerField()
	available=models.BooleanField()
	slug = models.SlugField(max_length=100)
	
	def slug(self):
		return slugify(self.category.name+'_'+self.name)

	def __str__(self):
		return self.name


class topitems(models.Model):
	product=models.ForeignKey('product')

	def __str__(self):
		return self.product.name
	class Meta:
		verbose_name_plural = "topitems"

class recommended(models.Model):
	product=models.ForeignKey('product')
	def __str__(self):
		return self.product.name
	class Meta:
		verbose_name_plural = "recommended"


class topcategory(models.Model):
	product=models.ForeignKey('category')

	def __str__(self):
		return self.product.name

	class Meta:
		verbose_name_plural = "topcategory"
