from decimal import Decimal
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, View
from django.contrib import messages

from orders.forms import DeliverAddress
from orders.models import OtherCharge
from products.models import Category, Product

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render

from django.urls import reverse
from django.views.decorators.http import require_POST
from .order import Cart
from .forms import CartAddProductForm

from django.contrib import messages
from django.db.models import Q

# Create your views here.
app_name = 'supply'


# Default Home List View
class HomeView(ListView):
    model = Product
    queryset = Product.objects.order_by('-product_created_on')
    template_name = "supply/index.html"
    
    def get_queryset(self):
        return Product.objects.order_by('-product_created_on')
    
    def get_context_data(self, **kwargs):
        
        cart = Cart(self.request)
        
        item_count = len(cart)
        context = super().get_context_data(**kwargs)
        context["featured_product"] = self.get_queryset().filter(product_is_featured=True)[:10]
        context['fruits_product_list'] = self.get_queryset().filter(product_category__slug='fruits')[:5]
        context['vegetables_product_list'] = self.get_queryset().filter(product_category__slug='vegetables')[:5]
        context['cereals_product_list'] = self.get_queryset().filter(product_category__slug='cereals')[:5]
        context['potatoes_product_lforist'] = self.get_queryset().filter(product_category__slug='potatoes')[:5]
        context['legumes_product_list'] = self.get_queryset().filter(product_category__slug='legumes')[:5]
        context["item_count"] = item_count
        
        return context

# All Categories

class AllCategories(ListView):
    model = Product
    queryset = Product.objects.order_by('-product_created_on')
    template_name = "supply/category/all_categories.html"
# Product Detail view
class ProductDetailView(DetailView):
    model = Product
    template_name = "supply/product.html"
    
    def get_context_data(self, **kwargs):
        
        cart = Cart(self.request)
        item_count = cart.item_count()
        
        context = super().get_context_data(**kwargs)
        context ['CartAddProductForm'] = CartAddProductForm()
        context["item_count"] = item_count
        
        return context
    
    
class CategoryList(ListView):
    template_name = 'supply/category/category_list.html'
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(
        product_category=self.category).order_by('-product_created_on')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_name"] = self.category.category_name
        context['category_product_list'] = self.get_queryset()
        context["category_description"] = self.category.category_desc
        return context
    
    
    
    
# creating orders
@login_required(login_url="/accounts/login")
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        cart.save()
    return redirect('supply:cart_detail')

# cart remove

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('supply:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    other_charges = get_object_or_404(OtherCharge)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm
        
        
    if request.method =='POST':
        delivery_address = DeliverAddress(request.POST, prefix='delivery_address')

        if delivery_address.is_valid():
            delivery_address.save()
            
        else:
            messages.info(request, 'Please correct errors')
    delivery_address = DeliverAddress()
    
    

    item_count = cart.item_count()
    return render(request, 'supply/order.html', 
                  {"cart": cart, 
                   "item_count": item_count,
                   "delivery_address": delivery_address,
                   "other_charges":other_charges})
 

