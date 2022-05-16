from django import forms
from django.forms import ModelForm, fields
from .models import Farmer, Customer



class FarmerCreate(forms.ModelForm):
    class Meta:
        model = Farmer
        exclude = ('farmer_login_id',)
        
        
        
class CustomerCreate(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('customer_login_id',)