from xml.dom.minidom import Document
from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from backend import settings
urlpatterns= [

path('',views.employeeApi),
#re_path(r'^employee/([0-9]+)$',views.employeeApi),
path('<int:id>',views.employeeApi),
path('SaveFile/',views.SaveFile),
path('bankname/',views.bank_names),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
