from django.contrib import admin
from bug.models import Bug

class BugAdmin(admin.ModelAdmin):
    list_display = ['bugname','bugdetail','bugstatus','buglevel','bugcreater','bugassign','create_time','update_time','ID']
# Register your models here.
admin.site.register(Bug)#把bug管理模块注册到Django admin 管理后台并显示