from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from orders.models import OtherCharge
from .models import Product
import urllib.request as urllib 

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'unit_price':str(product.product_unit_price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = int(quantity)
        else:
            self.cart[product_id]['quantity'] = int(quantity)
        self.save()
        
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
        
    def remove(self, product):
        product_id =str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
           self.cart[str(product.id)]['product'] = product
           
        for item in self.cart.values():
            item['unit_price'] = Decimal(item['unit_price'])
            item['total_price'] = item ['unit_price'] * item['quantity']
            yield item
            
            
    def __len__(self):
        return len([item for item in self.cart.values()])
    
    def item_count(self):
        return len(self)

    def unit_total (self):
        for item in self.cart.values():
            return (Decimal(item['unit_price']) * item['quantity'])
    
    def get_total_price(self):
        shipping = get_object_or_404(OtherCharge)
        shipping_cost = shipping.other_charge_rate
        total = sum(Decimal(item['unit_price']) * item['quantity'] for item in self.cart.values())
        total_price = int(total) + int(shipping_cost)
        return total_price

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
        
    def __str__(self) -> str:
        return f"{self.cart}"
    
        