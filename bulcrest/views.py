# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from serializer import *
from rest_framework.generics import ListAPIView

# Create your views here.
def index(request):
	print 1123123
	return HttpResponse('hello rest is ready')

def case(request):
	return HttpResponse('you have a good case ')

class productList(ListAPIView):
	serializer_class=productSerializer
	
	def get_queryset(self):
		"""
		"""
		queryset = product.objects.all()
		q = self.request.query_params.get('id', None)
		if q is not None:
			queryset =queryset.filter(caseId=q)
		return queryset

	