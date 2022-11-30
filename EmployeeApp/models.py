
from django.db import models

# Create your models here.


class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=150)
    DateOfJoining = models.DateField(auto_now_add=True)
    PhotoFileName = models.CharField(max_length=150)
class Bank(models.Model):
    SWIFT_CODE =  models.CharField(primary_key=True,max_length=150)
    bank_n =  models.CharField(max_length=150,null=True)
    Branch =  models.CharField(max_length=150,null=True)
    Adress = models.CharField(max_length=300,null=True)
    City = models.CharField(max_length=150,null=True)
    Country = models.CharField(max_length=150,null=True)
    bank_num = models.CharField(max_length=150,null=True)
    country_num = models.CharField(max_length=150,null=True)