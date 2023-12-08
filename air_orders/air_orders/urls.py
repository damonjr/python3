"""
URL configuration for air_orders project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import re_path as url
from django.contrib import admin
from django.urls import path
from air_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^hbl_list/', views.orders_list),
    path('hbl/', views.get_hbl), #获取HBL信息接口
    path('hbl/query/', views.query_hbl), #查询HBL接口
    path('hbl/check/', views.is_exsits_hblNum),#检查HBL号是否存在

]
