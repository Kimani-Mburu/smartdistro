from django import forms
from django.forms import ModelForm,fields

from orders.models import Payment, PurchaseOrder


from .models import Order

class DeliverAddress(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_delivery_address',)
        
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('payment_mode','payment_ref',)