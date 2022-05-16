from django import forms
from django.forms import ModelForm, fields
from .models import OtherCharge


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 50)]
        
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

