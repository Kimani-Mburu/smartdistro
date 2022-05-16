from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE
# Create your models here.
class Farmer(models.Model):
    farmer_login_id = models.ForeignKey(User, on_delete=CASCADE)
    farmer_first_name = models.CharField(max_length=20)
    farmer_last_name = models.CharField(max_length=20)
    farmer_national_id = models.IntegerField(null = False, blank = False)
    farmer_phone_no = PhoneNumberField(blank=True)
    farmer_email = models.EmailField()
    farmer_address = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return f"{self.farmer_first_name} {self.farmer_last_name}"
    
    
# Vendors profile

class Customer(models.Model):
    customer_login_id = models.ForeignKey(User, on_delete=CASCADE)
    customer_first_name = models.CharField(max_length=20)
    customer_last_name = models.CharField(max_length=20)
    customer_national_id = models.IntegerField(null = False, blank = False)
    customer_phone_no = PhoneNumberField(blank=True)
    customer_email = models.EmailField()
    customer_address = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return f'{self.customer_first_name}, {self.customer_last_name}'

