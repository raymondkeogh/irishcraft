from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):

    readonly_fields = ('title', 'body',
                       'product', 'user',
                       'created', 'updated')
    # sorty product by sku
    ordering = ('product',)

admin.site.register(Review, ReviewAdmin)
