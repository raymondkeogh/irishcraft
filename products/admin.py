"""
Product Admin Classes
"""
from django.contrib import admin
from .models import Product, Category


# Admin classes take from Code Institue Boutique Ado tutorial
class ProductAdmin(admin.ModelAdmin):
    """
    Product admin
    """
    list_display = (
        'name',
        'id',
        'category',
        'price',
        'rating',
        'image',
    )
    # sort product by sku
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Category Admin
    """
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
