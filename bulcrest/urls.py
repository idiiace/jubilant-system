from django.conf.urls import url,include

from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^products/', productList.as_view()),
    
]