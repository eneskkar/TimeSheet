"""Timesheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include,re_path
from django.urls import re_path as url
from Timeaapp import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='YOUR NAME'),
    url(r'^timesheet/([0-9]+)/(.*?)/(.*?)/(.*?)/([a-zA-Z]+)/([a-zA-Z]+)/([a-zA-Z]+)/([a-zA-Z]+)$',views.get_timesheet),
    url(r'^timesheet/(.*?)/list$', views.getTimeSheet),
    url(r'^timesheet/([0-9]+)/list$', views.get_id_timesheet),
    url(r'^user/login/([a-zA-Z]+)/([a-zA-Z]+)$', views.LogIn),
    url('user/check/', views.CheckLoginState),
    url(r'^timesheet/add/(.*?)/(.*?)/(.*?)/([a-zA-Z]+)/([a-zA-Z]+)/(.*?)/(.*?)$', views.AddTimeSheet),
    url('user/logout', views.LogOut),
    url(r'^timesheet/edit/([0-9]+)/(.*?)/(.*?)/(.*?)/([a-zA-Z]+)/([a-zA-Z]+)/(.*?)/(.*?)$', views.EditTimesheet),
    url(r'^timesheet/delete/([0-9]+)$', views.DeleteTimesheet)
]
