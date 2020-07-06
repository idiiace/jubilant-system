# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from functions.views import *


# Create your views here.
def add_to_cart_ajax(request,Id):
	add_to_cart(request,Id,1)
	return HttpResponse('successful')

def minus_cart_ajax(request,Id):
	add_to_cart(request,Id,-1)
	return HttpResponse('successful')

def signout(request):
	logout(request)


def index(request):
	get_cookie_custom(request)
	request.session._get_or_create_session_key()
	categories=return_categories()
	topcategories=get_top_categories()
	topproducts=get_topitems()
	recommended=get_recommended()

	All={'categories':categories,
	'popularcategories':topcategories,
	'popularproduct':topproducts,
	'recommended':recommended}

	return render(request,'index.html',All)

def loginpage(request):
	return render(request,'logintrue.html')


def get_verification(request):
	phonenumber = request.POST.get('phonenumber', '')
	code=get_verified_short_code(request,phonenumber)
	return HttpResponse('successful')

def signup(request):
	if request.method == "POST":
		create_user(request)
		return render(request,'verificationpage.html')
	else:
		return render(request,'signup.html')

def signuppage(request):

	return render(request,'signup.html')

def verify(request):
	return render(request,'verificationpage.html')


def cartpage(request):
	cart=get_cart(request)
	return render(request,'cart.html',cart)


def product(request,Id):
	pro= get_product(Id)[0]
	return render(request,'product.html',{'item':pro})

def productspage(request,Id=0):
	products=get_product_by_cat(Id)
	return render(request,'productpage.html',{'products':products})

def productspagewithid(request,Id=0):
	
	products=get_product_by_cat(Id)
	return render(request,'productpage.html',{'products':products})

def account(request):
	print request.user.id
	logged_in=User.objects.filter(id=request.user.id)

	return render(request,'accountinfo.html',dict(v=logged_in))

def ordertracking(request):
	return render(request,'ordertracking.html')
