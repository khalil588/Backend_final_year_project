from django.urls import  path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('profile/',views.ProfileView.as_view()),
    path('api/auth/', views.CustomAuthToken.as_view()),
   
]
urlpatterns = format_suffix_patterns(urlpatterns)