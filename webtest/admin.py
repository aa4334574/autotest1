from django.contrib import admin
from webtest.models import Webcase,Webcasestep

class WebcasestepAdmin(admin.TabularInline):
    list_display=['webteststep','webtestobjname','webfindmethod','webevelement','weboptmethod','webassertdata','webtestresult','createtime','updatetime','id','webcase']
    model = Webcasestep
    extra=1

class WebcaseAdmin(admin.ModelAdmin):
    list_display = ['webcasename', 'webtestresult','createtime','updatetime','id']
    inlines = [WebcasestepAdmin]
admin.site.register(Webcase,WebcaseAdmin)
# Register your models here.
