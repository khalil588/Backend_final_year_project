from curses import meta
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from EmployeeApp.models import Bank, Employee



class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = ('EmployeeId',
        'EmployeeName',
        'DateOfJoining',
        'PhotoFileName')

class BankSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bank
        fields = ('SWIFT_CODE',
        'bank_n',
        'Branch',
        'Adress',
        'City',
        'Country',
        'bank_num',
        'country_num')