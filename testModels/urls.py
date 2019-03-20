#coding utf-8
#author: pengweijian
#date: 2019/3/13

from django.contrib import admin
from django.urls import path
from testModels import views
urlpatterns = [
    # 根据app对路由规则进行分类
    path('addBookInfo/', views.add_book_info),
]