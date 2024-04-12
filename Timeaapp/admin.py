from django.contrib import admin

# Register your models here.

from .models import Timesheet, Employee, Customer
admin.site.register(Timesheet)
admin.site.register(Employee)
admin.site.register(Customer)

