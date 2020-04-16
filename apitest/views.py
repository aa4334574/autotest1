"""
视图，创建视图函数
"""
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect#加入引用
#from django.contrib.auth.decorators import login_required #登录模块
from django.contrib import auth
#from django.contrib.auth import authenticate,login
# Create your views here.
def test(request):
    """
    映射函数
    """
    return HttpResponse('hello WORD')#返回HTTPResponse响应函数
def login(request):
    """
    映射函数，登录
    """
    if request.POST:
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user']=username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request,'login.html',{'error':'username or password error'})
    return render(request,'login.html')#跳转到对应的页面
def home(request):
    """
    跳转主页
    """
    return render(request,'home1.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')