from datetime import date
from django.db import models

# Create your models here.

class Employee(models.Model):
    name= models.CharField(max_length=20)
    surname= models.CharField(max_length=20)
    def __str__(self):
        return '%s %s' % (self.name, self.surname)
    
class Customer(models.Model):
    customer_name= models.CharField(max_length=20)
    def __str__(self):
        return '%s' % (self.customer_name)


class Timesheet (models.Model):
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    project= models.CharField(max_length=30)
    date= models.DateField()
    hour1= models.TimeField()
    hour2= models.TimeField()
    activity= models.CharField(max_length=255)
    description= models.CharField(max_length=255)

