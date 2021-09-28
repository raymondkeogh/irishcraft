"""Product Activity Admin setttings"""
from django.contrib import admin

from .models import ProductActivity


class ProductActivityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'view_count',
        'purchase_count',
        'viewed_on',

    )
    # sorty product by sku
    ordering = ('name',)


admin.site.register(ProductActivity, ProductActivityAdmin)
