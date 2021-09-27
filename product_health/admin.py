from django.contrib import admin
from checkout.models import OrderLineItem
from checkout.admin import OrderLineItemAdminInline

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
