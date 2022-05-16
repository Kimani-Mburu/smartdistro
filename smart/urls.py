from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.decorators.cache import cache_control
from django.contrib.staticfiles.views import serve



urlpatterns = [
     path('admin/', admin.site.urls),
     path("", include("supply.urls", namespace="supply")),
     path("accounts/", include('accounts.urls')),
     path('user-profiles',include("UserInformation.urls", namespace="user-information")),
     path('products/', include('products.urls', namespace= 'products')),
     path('orders/', include('orders.urls', namespace='orders')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
admin.site.site_header = "Smart Crop Distro"
admin.site.site_title = "Smart Crop Distro Admin Portal"
admin.site.index_title = "Welcome to Smart Crop Distro"


class SomeModelAdmin(admin.ModelAdmin):
    
    def admin_action(self, request, queryset):
         actions = ["export_as_csv"]

