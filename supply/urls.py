from django.urls import path
from .views import AllCategories,HomeView, ProductDetailView, CategoryList
from . import views

app_name = "supply"




urlpatterns = [
    # Home view
    
    path('', HomeView.as_view(), name='home'),
# Product detail view
    path('product/<pk>/', ProductDetailView.as_view(), name ="product"),
    path('category/<slug>/', CategoryList.as_view(), name='category'),
    path('all', AllCategories.as_view(), name="all-categories"),
# Cart functions, adding, removing and updating products in cart

    path('cart_add/<product_id>', views.cart_add, name="cart_add"),
    path('cart_remove/<product_id>',views.cart_remove, name="cart_remove"),
    path('cart_detail/', views.cart_detail, name="cart_detail"),
    ]