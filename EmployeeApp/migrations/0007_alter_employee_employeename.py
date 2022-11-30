# Generated by Django 4.0.4 on 2022-05-11 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EmployeeApp', '0006_alter_employee_employeename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmployeeName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
