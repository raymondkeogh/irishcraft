from django.contrib import admin
from checkout.models import OrderLineItem
from checkout.admin import OrderLineItemAdminInline

from .models import ProductActivity, PurchaseHistory

class ProductActivityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'view_count',
        'viewed_on',
    )
    # sorty product by sku
    ordering = ('name',)

class PurchaseHistoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )
    ordering = ('name',)


admin.site.register(ProductActivity, ProductActivityAdmin)
admin.site.register(PurchaseHistory, PurchaseHistoryAdmin)
