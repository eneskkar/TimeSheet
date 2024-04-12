from rest_framework import serializers
from Timeaapp.models import  Timesheet, Employee, Customer



class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Timesheet
        fields=('employee','customer','project','date','hour1','hour2','activity','description')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee 
        fields=('name','surname')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('customer_name')

          