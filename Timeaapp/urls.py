from django.urls import path,include, re_path
from Timeaapp import views
from django.urls import re_path as url


from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^timesheet$',views.get_timesheet),
    url(r'^Timeaapp/([0-9]+)$',views.get_timesheet),

]