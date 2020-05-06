from django.contrib import admin as new_admin
from apptest.models import Appcase,Appcasestep

# Register your models here.

class AppcasestepAdmin(new_admin.TabularInline):
    list_diaplay = ['appteststep','apptestobjname','appfindmethod','appevelement','appoptmethod','apptestdata','appassertdata','apptestresult','create_time','update_time','id','appcase']
    model = Appcasestep
    extra = 1

class AppcaseAdmin(new_admin.ModelAdmin):
    list_display = ['appcasename','apptestresult','create_time','update_time','id']
    inlines = [AppcasestepAdmin]


new_admin.site.register(Appcase,AppcaseAdmin)
# new_admin.site.register(Appcase,Appcasestep) 为什么是失败