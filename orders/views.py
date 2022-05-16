from django.contrib.auth.models import User
from django.core.checks import messages

from django.core.mail import send_mail
from products.models import Product
from smart.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage



from django.shortcuts import get_object_or_404, redirect, render
from UserInformation.models import Customer
from django.template import Context
from django.template.loader import render_to_string

from orders.models import Order, Order_item, Order_other_charge, OtherCharge
from supply.order import Cart
from orders.models import PurchaseOrder, Payment
from .forms import PaymentForm


app_name = 'orders'
  
def checkout(request):
    cart = Cart(request)
    item_count = len(cart)
    user  = get_object_or_404(User, id=request.user.id)
    customer = get_object_or_404(Customer, customer_login_id=user)
    order_charges = get_object_or_404(OtherCharge)
    
   
   
    if len(cart):
        # create an order
        order = Order.objects.create(order_customer_login_id=user, order_customer_id=customer, order_delivery_address = 'Ouga, Nyeri')
        order.save()
        
        # get items from cart and add them to order items
        for item in cart:
            total = (int(item['unit_price']) * item['quantity'])
            total_cost = int(total) + 500
            order_item = Order_item.objects.create(
                order_item_order_id = order,
                order_item_product_id = item['product'],
                order_item_quantity = item['quantity'],
                order_item_total_cost = (int(item['unit_price']) * item['quantity'])
            )
            order_item.save() 
            
            
            
        # Query for order items in an order
        ref_no = order
        order_items = Order_item.objects.filter(order_item_order_id = ref_no)
        for order_item in order_items:
            product_id = order_item.order_item_product_id
            
            
            
        # send email to customer
        
        customer_email =  customer.customer_email
        
        
        # send email to farmer  
        farmer = product_id.product_farmer_login_id
        email = farmer.farmer_email
        
        
        subject = "New Order Alert"
        to = [email]
        from_email = EMAIL_HOST_USER

        ctx = {
        'farmer': farmer,
        'order': order,
        'order_item':order_item
        }

        message = 'New Order Alert. Please prepare for order delivery within 48 hrs.'

        EmailMessage(subject, message, to=to, from_email=from_email).send()

     
        # OtherCharges for the order
        
        order_other_charges = Order_other_charge.objects.create(
            order_other_charge_charges_id = order_charges,
            order_other_charge_order_id = order,
            order_other_charge_total_price = order_charges.other_charge_rate
        )
        order_other_charges.save()
        
        
        
        # create a purchase order
        
        
        purchase = PurchaseOrder.objects.get_or_create(
        purchase_order_Order_id = order,
        purchase_order_Other_charges = order_other_charges,
        purchase_order_total_value = total_cost
        )
        
        
        context = {
            'cart': cart,
            'order':order,
            'customer': customer,
            'reference_no': ref_no,
            'order_items': order_items,
            'delivery_address': order.order_delivery_address,
            'order_date': order.order_date,
            'item_count':item_count
        }
        return render(request,'supply/checkout.html', context )
    else:
            return redirect('supply:cart_detail')


# create a purchase order

def payment(request):
    cart = Cart(request)
    user = get_object_or_404(User, id = request.user.id)
    order = get_object_or_404(Order.objects.filter(order_customer_login_id = user)[:1])
    
    for item in cart:
            total = (int(item['unit_price']) * item['quantity'])
            total_cost = int(total) + 500
    if request.method == 'POST':
            form = PaymentForm(request.POST)
            
            if form.is_valid:
                form = form.save(commit=False)
                
                payment = Payment.objects.create(
                    payment_mode = form.payment_mode,
                    payment_total_price = total_cost,
                    payment_ref = form.payment_ref,
                    payment_order_id = order
                )
                
                
                return redirect('orders:success')
            else:
                messages.error(request, 'Error while confirming your payment. Please try again')
          
    
    form = PaymentForm()  
    context = {
        'form':form,
    }
    
    return render(request, 'supply/success.html', context)


def success(request):
    user =get_object_or_404(User, id = request.user.id)
    customer = get_object_or_404(Customer, customer_login_id = user)
    return render(request, 'supply/payment.html', {'customer':customer})