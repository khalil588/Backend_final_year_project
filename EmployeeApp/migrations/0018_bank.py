# Generated by Django 4.0.4 on 2022-05-12 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0017_rename_employeename_id_employee_employeename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('SWIFT_CODE', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('bank_n', models.CharField(max_length=150)),
                ('Branch', models.CharField(max_length=150)),
                ('Adress', models.CharField(max_length=150)),
                ('City', models.CharField(max_length=150)),
                ('State', models.CharField(max_length=150)),
                ('Country', models.CharField(max_length=150)),
                ('bank_num', models.CharField(max_length=150)),
                ('country_num', models.CharField(max_length=150)),
            ],
        ),
    ]