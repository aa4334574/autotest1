from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from apptest.models import Appcase,Appcasestep
# Create your views here.
@login_required
def appcase_manage(request):
    """APP用例管理跳转函数"""
    appcase_list = Appcase.objects.all()
    username = request.session.get('user','')#读取浏览器session
    return render(request,'appcase_manage.html',{'user':username,'appcases':appcase_list})

@login_required
def appcasestep_manage(request):
    """用例步骤管理跳转函数"""
    appcasestep_list = Appcasestep.objects.all()
    username = request.session.get('user','')
    return render(request,'appcasestep_manage.html',{'user':username,'appcasesteps':appcasestep_list})
