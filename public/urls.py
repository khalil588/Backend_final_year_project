from django.urls import  path
from rest_framework.urlpatterns import format_suffix_patterns
from public import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('',views.IndexView.as_view()),
   
]
urlpatterns = format_suffix_patterns(urlpatterns)