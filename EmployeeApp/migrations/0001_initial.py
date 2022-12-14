# Generated by Django 4.0.4 on 2022-04-29 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=150)),
                ('Department', models.CharField(max_length=100)),
                ('DateOfJoining', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=150)),
            ],
        ),
    ]
