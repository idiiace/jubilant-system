from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.


class productsAdmin(admin.ModelAdmin):
    model = product
    list_display =['name','instock', 'category','price','available']
    



admin.site.register(product, productsAdmin)
admin.site.register(category)
admin.site.register(topitems)
admin.site.register(recommended)
admin.site.register(topcategory)

