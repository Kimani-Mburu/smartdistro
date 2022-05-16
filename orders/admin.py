from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import OtherCharge, Order, Order_item, Order_other_charge, PurchaseOrder, Payment

class OrderAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['order_customer_login_id', 'order_date', 'order_delivery_address']
    
    
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_item)
admin.site.register(OtherCharge)
admin.site.register(Order_other_charge)

class PaymentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['payment_mode', 'payment_total_price', 'payment_order_id']

admin.site.register(Payment, PaymentAdmin)

class PurchaseAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['purchase_order_date', 'purchase_order_total_value','purchase_order_status']

admin.site.register(PurchaseOrder, PurchaseAdmin)