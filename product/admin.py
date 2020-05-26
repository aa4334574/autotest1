from django.contrib import admin
from product.models import Product
# from webtest.models import Webcase

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter','create_time','id']
    admin.site.register(Product)#将Product模块注册到admin后台中，并能显示。


# class WebcaseAdmin(admin.TabularInline):
#     list_display = ['webcasename', 'webtestresult','create_time','id','product']
#     model = Webcase
#     extra = 1
# Register your models here.
