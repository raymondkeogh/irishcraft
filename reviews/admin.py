# Review Admin settings
from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """Review admin display setttings"""
    list_display = (
        'product',
        'title',
        'user',
        'rating'
    )

    readonly_fields = ('title', 'body',
                       'product', 'user',
                       'created', 'updated')
    # sort product by product
    ordering = ('product',)


admin.site.register(Review, ReviewAdmin)
