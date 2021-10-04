"""
Product Activity model
"""
from django.db import models

from django.conf import settings

from products.models import Product


user = settings.AUTH_USER_MODEL


class ProductActivity(models.Model):
    """
    A model to keep track of product activity on the site
    """
    name = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='producty_activity')
    view_count = models.PositiveIntegerField(default=0)
    purchase_count = models.PositiveIntegerField(default=0)
    viewed_on = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Product Activity"
