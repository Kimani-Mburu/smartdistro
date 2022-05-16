from django.urls import path

from . import views


app_name = "products"

urlpatterns = [
    path('Create-product', views.add_product, name="add-product")
]
