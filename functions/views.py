# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from products.models import product,category,topcategory,topitems,recommended
from verification.models import verifaction_tracking,user_is_veried,User
from django.contrib.auth import authenticate, login,logout
from cart.cart import Cart
from functions.smsmodule import Message,SMSGateway


def get_cart(request):
	
	return dict(cart=Cart(request),summmary=Cart(request).summary())



def get_cookie_custom(request):
	request.session._get_or_create_session_key()

def get_verified_short_code(request,phonenumber):
	code=random.randint(100000,999999)
	get_cookie_custom(request)
	sessionid=request.COOKIES['csrftoken']
	a=verifaction_tracking(phonenumber=phonenumber,sessionid=sessionid,verfication_code=code,verified=False)
	a.save()
	send_sms(code,phonenumber)

def create_user(request):
	phonenumber = request.POST.get('phonenumber', '')
	firstname= request.POST.get('firstname', '')
	secondname=request.POST.get('lastname', '')
	account=User(username=phonenumber,first_name=firstname,last_name=secondname,password="1234")
	account.save()
	a=user_is_veried(username=account,is_veried=False)
	a.save()
	get_verified_short_code(request,phonenumber)

def add_to_cart(request, product_id,quantity):
    Product = product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(Product, Product.price, quantity)
    print "successfully added ",Product



def verify_code(request):
	code = int(request.POST.get('code', ''))
	get_cookie_custom(request)
	sessionid=request.COOKIES['csrftoken']
	l=verifaction_tracking.objects.filter(sessionid=sessionid)

	if l:
		if code==verifaction_tracking.objects.filter(sessionid=sessionid)[0].verfication_code:
			d=verifaction_tracking.objects.filter(sessionid=sessionid)[0]
			d.verified=True
			d.save()
			phonenumber=d.phonenumber
			username=User.objects.filter(username=phonenumber)[0]
			login(request,username)
			return render(request,"index.html")
		else:
			return HttpResponse('Wrong verification code please try again')
	else:
		return render(request,'404.html')

def send_sms(code,number):
	 a=SMSGateway('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTU0MzA0NzI0MSwiZXhwIjo0MTAyNDQ0ODAwLCJ1aWQiOjY0NTY1LCJyb2xlcyI6WyJST0xFX1VTRVIiXX0.uJfURu3qZ3N5ew1sqR_bYD1EhO9A44fLXIsX0vNUUEs')
	 msg=Message(str(number),str(code),'105854')
	 a.send_sms(msg)


def get_product(i):
	return product.objects.filter(id=i)
def return_categories():
	return category.objects.all()

def get_product_by_cat(Id=0):
	if Id:
		
		a=product.objects.filter(category=Id)
		return a
	else:
		return product.objects.all()

def get_topitems():
	p=[]
	count=0
	for i in topitems.objects.all():
		if count==5:
			return topitems.objects.all()
		else:
			p.append(i)
			count+=1

def get_top_categories():
	p=[]
	count=0
	for i in topcategory.objects.all():
		if count==3:
			return topcategory.objects.all()
		else:
			p.append(i)
			count+=1

def get_recommended():
	p=[]
	count=0
	for i in recommended.objects.all():
		if count==3:
			return recommended.objects.all()
		else:
			p.append(i)
			count+=1

