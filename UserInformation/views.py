from django.contrib.messages.api import error
from django.shortcuts import render

from products.models import Product
from .models import Farmer, Customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import FarmerCreate, CustomerCreate
# Create Farmer View

@login_required(login_url="/accounts/login")

def create_farmer(request):
    user = get_object_or_404(User, id=request.user.id)
    # Check if user has a farmer profile
    farmer_qs = Farmer.objects.filter(farmer_login_id=user)
    
    if farmer_qs.exists():
        return redirect ('products:add-product')
    else:
        if request.method == 'POST':
            form = FarmerCreate(request.POST)
            
            if form.is_valid:
                form = form.save(commit=False)
                form.farmer_login_id = request.user
                form.save()
                
                # Print success message
                messages.info(request,'Farmer Profile created successfully')
                return redirect('products:add-product')
            else:
                # print error message
                messages.error(request,'Error occured while creating Farmer profile. Please try again.')
                
                return redirect('user-information:create-farmer')
        
        form = FarmerCreate()
        return render(request,'createfarmer.html', {'form':form})
    
def create_customer(request):
    user = get_object_or_404(User, id=request.user.id)
    
    # check if user has a customer account
    
    customer_qs = Customer.objects.filter(customer_login_id=user)
    
    if customer_qs.exists():
        return redirect('orders:checkout')
    
    else:
        if request.method == 'POST':
            form = CustomerCreate(request.POST)
            
            if form.is_valid:
                form = form.save(commit=False)
                form.customer_login_id = request.user
                form.save()
                
                # Success Message
                messages.info(request,'Customer profile created successfully')
                return redirect('orders:checkout')
            
            else:
                messages.error(request, 'Error occured while creating profile')
                return redirect('user-information:create-customer')
            
        form = CustomerCreate()
        return render(request, 'createcustomer.html',{'form':form})
    
    
def profile(request, user, object):
    user = get_object_or_404(User, id=request.user.id)
    
    
    object = Product.objects.filter(product_farmer_login_id = user.id)
    if object.exists:
        farmer = get_object_or_404(farmer_login_id=user)
        context = {
            'user':user,
            'object':object,
            'farmer':farmer
        }
        return render(request, 'accounts/profile.html', context)
    
    else:
        return redirect('supply:home')