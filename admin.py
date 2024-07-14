from django.contrib import admin
from .models import Vendor, Product

class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_name', 'user', 'website_url', 'profile_picture')
    search_fields = ('vendor_name', 'user__username')
    list_filter = ('user',)
    ordering = ('vendor_name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor', 'description', 'pdf_document')
    search_fields = ('name', 'vendor__vendor_name', 'description')
    list_filter = ('vendor',)
    ordering = ('name',)

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Product, ProductAdmin)

