from django import forms
from django.forms import ModelForm, fields
from .models import Product


class ProductsAdd(forms.ModelForm):
    class Meta:
       model = Product
       exclude = ('product_is_featured','product_created_on','farmer_login_id')
       
