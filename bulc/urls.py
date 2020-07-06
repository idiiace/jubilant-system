"""bulc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from viewscentral.views import *
from bulcrest.urls import urlpatterns as resturls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest/', include(resturls)),
    url(r'^$', index,name="home"),
    url(r'^login/', loginpage),
    url(r'^details/(?P<Id>\d+)/$', product),
    url(r'^cart/', cartpage),
    url(r'^signup/', signuppage),
    url(r'^signout/', signout),
    url(r'^products/(?P<Id>\d+)/$', productspagewithid),
    url(r'^products/', productspage),
    url(r'^verify/', verify),
    url(r'^orderandtracking/', ordertracking),
    url(r'^account/', account),
    url(r'^verificationcode/', get_verification),
	url(r'^register/', signup),
	url(r'^verifycode/', verify_code),
    url(r'^add_to_cart_ajax/(?P<Id>\d+)/$', add_to_cart_ajax),
    url(r'^minus_cart_ajax/(?P<Id>\d+)/$', minus_cart_ajax),



]
