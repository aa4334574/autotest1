"""
视图，创建视图函数
"""
import pymysql
from apitest.models import Apitest, Apistep
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect  # 加入引用
from django.contrib.auth.decorators import login_required  # 登录模块
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 分页处理


# from models import Apitest
# from django.contrib.auth import authenticate,login
# Create your views here.
def test(request):
    """
    映射函数
    """
    return HttpResponse('hello WORD')  # 返回HTTPResponse响应函数


def login(request):
    """
    映射函数，登录
    """
    if request.POST:
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})
    return render(request, 'login.html')  # 跳转到对应的页面


def home(request):
    """
    跳转主页
    """
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


# 接口管理
@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all()  # 对其所有流程接口数量
    username = request.session.get('user', '')  # 读取浏览器登录的session
    paginator = Paginator(apitest_list, 1)  # 每8条生成一页
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第一页
    currentPage = int(page)  # 把获取的当前页码数转化成整数
    try:
        apitest_list = paginator.page(page)  # 获取当前页码的数据列表
    except PageNotAnInteger:
        apitest_list = paginator.page(1)  # 如果输入的不是整数，则默认返回第一页的数据
    except EmptyPage:
        apitest_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，则显示最后页
    return render(request, 'apitest_manage.html', {'user': username, 'apitests': apitest_list})  # 定义流程接口的变量，并返回给前端


# 流程步骤（单个接口）
@login_required
def apistep_manage(request):
    username = request.session.get('user', '')
    apistep_list = Apistep.objects.all()
    paginator = Paginator(apistep_list, 2)  # 每8条生成一页
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第一页
    currentPage = int(page)  # 把获取的当前页码数转化成整数
    try:
        apistep_list = paginator.page(page)  # 获取当前页码的数据列表
    except PageNotAnInteger:
        apistep_list = paginator.page(1)  # 如果输入的不是整数，则默认返回第一页的数据
    except EmptyPage:
        apistep_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，则显示最后页
    return render(request, 'apistep_manage.html', {'user': username, 'apisteps': apistep_list})  # 定义用例步骤的变量，并返回给前端


# api测试报告
@login_required
def test_report(request):
    username = request.session.get('user', '')
    apis_list = Apistep.objects.all()
    apis_count = Apistep.objects.all().count()  # 统计接口数
    db = pymysql.connect(user='root', db='autotest', passwd='123456', host='127.0.0.1')
    cursor = db.cursor()
    sql1 = 'SELECT count(id) FROM apitest_apitest WHERE apitest_apitest.apitestresult=1'
    aa = cursor.execute(sql1)
    apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
    sql2 = 'SELECT count(id) FROM apitest_apitest WHERE apitest_apitest.apitestresult=0'
    bb = cursor.execute(sql2)
    apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    db.close()
    return render(request, "api_report.html",
                  {"user": username, "apiss": apis_list, "apiscounts": apis_count, "apis_pass_counts": apis_pass_count,
                   "apis_fail_counts": apis_fail_count})  # 把值赋给apiscounts 变量


def left(request):
    return render(request, "left.html")


# 接口的搜索功能
@login_required
def apisearch(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    search_apitestname = request.GET.get("apitestname", "")
    apitest_list = Apitest.objects.filter(apitestname__icontains=search_apitestname)
    return render(request, 'apitest_manage.html', {"user": username, "apitests": apitest_list})


# 步骤的搜索
@login_required
def apistepsearch(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    search_apiname = request.GET.get("apiname", "")
    apistep_list = Apistep.objects.filter(apiname__icontains=search_apiname)
    return render(request, 'apistep_manage.html', {"user": username, "apisteps": apistep_list})
