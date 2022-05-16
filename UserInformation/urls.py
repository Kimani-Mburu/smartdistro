from django.urls import path
from . import views

app_name = "UserInformation"


urlpatterns = [
     path('create-customer/', views.create_customer, name='create-customer'),
     path('create-farmer/', views.create_farmer, name='create-farmer'),
     path('profile/', views.profile, name="profile")
]
