from re import S
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from EmployeeApp.models import Employee,Bank
from EmployeeApp.serializers import EmployeeSerializer,BankSerializer
import shutil
import subprocess
import os 
import pandas as pd
import openpyxl
from django.http import HttpResponse
import mimetypes
import glob
import time

# Create your views here.

def ls_file(link):
    y = glob.glob(link)
    return y


#searching for the newest file
def finding_creation_date(x):

    ti_c = os.path.getctime(x)
    c_ti = time.ctime(ti_c)

    # Using the timestamp string to create a
    # time object/structure
    t_obj = time.strptime(c_ti)

    # Transforming the time object to a timestamp
    # of ISO 8601 format
    T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
    return T_stamp
def files_date(link ="c:/frais/bd_src/*.xlsx"):
    z = {}
    df = pd.DataFrame(ls_file(link), columns=['names'])
    df['creation_time'] = df.apply(lambda df : finding_creation_date(df['names']),axis=1)
    x = df['creation_time'].max()
    y = df.loc[df['creation_time']==x,'names'].values.item()
    z[y] = df.loc[df['names']==y,'creation_time'].values.item()
    return z


def run_code():
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_BANK_0.1/dim_BANK/dim_BANK_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_COUNTRY_0.1/dim_COUNTRY/dim_COUNTRY_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_CURRENCY_0.1/dim_CURRENCY/dim_CURRENCY_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_DATE_0.1/dim_DATE/dim_DATE_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_FOLDER_0.1/dim_FOLDER/dim_FOLDER_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_REFERENCE_0.1/dim_REFERENCE/dim_REFERENCE_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_STATUS_0.1/dim_STATUS/dim_STATUS_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_UNIT_0.1/dim_UNIT/dim_UNIT_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/FACT_CHANGE_0.1/FACT_CHANGE/FACT_CHANGE_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/FACT_BANK_0.1/FACT_BANK/FACT_BANK_run.bat'])
   


def delete_last_line():
    df = pd.read_excel(open('C:/frais/files_name_date/files_bd_name_date.xlsx','rb'),sheet_name='sheet1')
    df = df.iloc[:-1 , :]
    with pd.ExcelWriter('C:/frais/files_name_date/files_bd_name_date.xlsx') as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)


def change_bd_src():
    delete_last_line()
    workbook=openpyxl.load_workbook('C:/frais/bd_src/bd_interm/bd_interm_hist/bd_interm_hist.xlsx')
    x = workbook.sheetnames
    print(x[len(x)-1])
    df = pd.read_excel(open('C:/frais/bd_src/bd_interm/bd_interm_hist/bd_interm_hist.xlsx','rb'),sheet_name=x[len(x)-1])
    with pd.ExcelWriter('C:/frais/bd_src/bd_interm/bd_interm.xlsx') as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)
    run_code()
    del workbook[x[len(x)-1]]
    workbook.save('C:/frais/bd_src/bd_interm/bd_interm_hist/bd_interm_hist.xlsx')



@csrf_exempt


def employeeApi(request,id = 0):
    if request.method == 'GET':
        employee = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee,many = True)
        return JsonResponse(employee_serializer.data,safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
 
        employee_serializer = EmployeeSerializer(data = employee_data)
        if employee_serializer.is_valid():
           employee_serializer.save()
           
           return JsonResponse('fichier ajouté avec succèes!!',safe=False)
        return JsonResponse(' ajout non effectué ',safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId = employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee,data = employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
        
            return JsonResponse('mise à jour avec succèes!!',safe=False)
        return JsonResponse('mise a jout non effectué' ,safe=False)
    elif request.method =='DELETE':
        employee =Employee.objects.get(EmployeeId = id)
        file_name =next(iter(files_date()))
        os.remove(file_name)
        change_bd_src()
        employee.delete()
        return JsonResponse('supprimé avec succèes', safe= False)

def movefile(f_name):
    f_src=r"C:/frais/projet_angular+django/backend/media/"+f_name
    f_ds =r"C:/frais/bd_src/"+f_name
    shutil.move(f_src,f_ds)
    return 0

@csrf_exempt

def SaveFile(request):
    file = request.FILES['uploadfile']
    file_name = default_storage.save(file.name,file)
    movefile(file.name)
    run_code()
    return JsonResponse(file_name,safe=False)
    
def modifyFile(x) :
    y = x[:8]
    df = pd.read_excel(open('C:/frais/bd_src/bd_interm/bd_interm.xlsx','rb'),sheet_name='sheet1')
    df = df[['COMPANY','RECID','CUSTOMER_NO','LR_ID_DEST','CHARGE_CCY','TOTAL_CHG_AMT','SWIFT_BQ_DEST','RELATED_REF','LR_REF_CORRESP','STATUS','REGULAR_DATE','SWIFT_BQ_REG']]
    df = df[(df['SWIFT_BQ_DEST'].str.startswith(y,na=False))]
    with pd.ExcelWriter('C:/frais/projet_angular+django/ui/front/src/assets/download.xlsx') as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)



@csrf_exempt
def bank_names(request):
    if request.method == 'GET':
        bank = Bank.objects.all()
        bank_serializer = BankSerializer(bank,many = True)
        return JsonResponse(bank_serializer.data,safe=False)
    elif request.method == 'POST':
        bank_data = JSONParser().parse(request)
        bank_swift = bank_data['SWIFT_CODE']
        modifyFile(bank_swift)
    return JsonResponse (' fichier ajoutée avec succèes',safe=False)