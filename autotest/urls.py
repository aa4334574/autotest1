"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apitest import views#加入引用，准备创建映射

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',views.test), #加入路径与关联函数。test为路径，views.test,是apptest中views的函数test
    path('login/',views.login),  #创建关联映射
    path('home/',views.home),
    path('logout/',views.logout),
]