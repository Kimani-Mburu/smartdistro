from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4

from datetime import date, datetime

from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices

from UserInformation.models import Customer
from products.models import Product


class OtherCharge(models.Model):
    other_charge_name = models.CharField(max_length=20)
    other_charge_desc = models.CharField(max_length=50)
    other_charge_rate = models.FloatField(default='0')
    
    def __str__(self):
        return self.other_charge_name
 
   
class Order(models.Model):
    order_customer_login_id = models.ForeignKey(User, on_delete=CASCADE)
    order_date = models.DateTimeField(default=datetime.now)
    order_reference_no = models.CharField(max_length=12, null=True, blank=True)
    order_customer_id = models.ForeignKey(Customer, on_delete=CASCADE)
    order_delivery_address = models.CharField(max_length=30, verbose_name='Delivery Address')
    
    def save(self, *args, **kwargs):
        if self.order_reference_no is None:
            uuid = str(uuid4())

            ref_no = uuid.split('-')[0].upper()
            self.order_reference_no = ref_no
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{str(self.order_reference_no)}"
    
class Order_item(models.Model):
    order_item_order_id = models.ForeignKey(Order, on_delete=CASCADE)
    order_item_product_id = models.ForeignKey(Product, on_delete=CASCADE)
    order_item_quantity = models.IntegerField(default=1)
    order_item_total_cost = models.FloatField()
    
    def __str__(self):
        return f"{str(self.order_item_order_id)}"
class Order_other_charge(models.Model):
    order_other_charge_charges_id = models.ForeignKey(OtherCharge, on_delete=CASCADE)
    order_other_charge_order_id = models.ForeignKey(Order, on_delete=CASCADE)
    order_other_charge_total_price = models.FloatField()
    
    def __str__(self):
        return f"{str(self.id)}"


STATUS = (
    ('Shipped','Shipped'), ('Canceled','Canceled'), ('On-route','On-route'),('Delivered','Delivered')) 

class PurchaseOrder(models.Model):
    purchase_order_Order_id = models.ForeignKey(Order, on_delete=CASCADE)
    purchase_order_Other_charges = models.ForeignKey(Order_other_charge, on_delete=CASCADE)
    purchase_order_date = models.DateField(default=date.today)
    purchase_order_total_value = models.FloatField()
    purchase_order_status = models.CharField(max_length=10, choices=STATUS)
    
    
    def __str__(self):
        return f"{str(self.purchase_order_Order_id)}"
    
    
    
    
PAY = (('M-pesa','M-pesa'),('Cash','Cash'))
class Payment(models.Model):
    payment_mode = models.CharField(max_length=10, choices=PAY, verbose_name='Payment')
    payment_total_price = models.FloatField()
    payment_ref = models.CharField(max_length=10, blank=True, null=True, verbose_name=' M-pesa Transaction code')
    payment_order_id = models.CharField(max_length=10)
    
    
    def save(self, *args, **kwargs):
        if self.payment_ref is None:
            uuid = str(uuid4())
            
            ref = uuid.split('-')[0].upper()
            self.payment_ref = ref
            
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return f"{str(self.payment_ref)}"
    

