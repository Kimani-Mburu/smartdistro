from django.contrib import admin
from .models import Farmer, Customer
from import_export.admin import ImportExportMixin

class FarmerAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['farmer_first_name', 'farmer_last_name', 'farmer_national_id','farmer_login_id']

admin.site.register(Farmer, FarmerAdmin)



class CustomerAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['customer_first_name', 'customer_last_name', 'customer_national_id','customer_login_id']
admin.site.register(Customer, CustomerAdmin)
