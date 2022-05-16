from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect

from UserInformation.models import Farmer
from .forms import ProductsAdd
from django.contrib import messages

app_name = "products"

def add_product(request):
    user = get_object_or_404(User, id=request.user.id)
    
    farmer = get_object_or_404(Farmer, farmer_login_id=user)
    
    if request.method == 'POST':
        product_form = ProductsAdd(request.POST, request.FILES)
        if product_form.is_valid():
            product_form = product_form.save(commit=False)
            product_form.farmer_login_id = farmer
            product_form.save()
            messages.info(request,'Product added successfully')
            return redirect('supply:home')
        else:
            messages.error(request, 'Error adding product. Please try again')
    
    product_form = ProductsAdd()
    
    return render(request,'supply/addproduct.html', {'product_form':product_form})
  
def test(request):
    return redirect('supply:home')