from django.contrib import admin
from product.models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter','create_time','id']
    admin.site.register(Product)#将Product模块注册到admin后台中，并能显示。
# Register your models here.
