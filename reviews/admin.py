from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    
    list_display = (
        'product',
        'title',
        'user',
    )

    readonly_fields = ('title', 'body',
                       'product', 'user',
                       'created', 'updated')
    # sorty product by product
    ordering = ('product',)


admin.site.register(Review, ReviewAdmin)
