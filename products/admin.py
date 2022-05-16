from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Category, Unit, Product

class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['product_name', 'product_description', 'product_category','product_unit_price', 'product_farmer_login_id']

admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Product, ProductAdmin)

