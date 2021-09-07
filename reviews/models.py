from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='reviews', related_query_name='reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews', related_query_name='reviews')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
