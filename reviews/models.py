"""
Review Model
"""
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# I fount this tutorial very helpful when creating the review model
# https://www.codementor.io/@jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a
class Review(models.Model):
    """
    Review Model class
    """
    ratings = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    title = models.CharField(
        max_length=255,
        blank=False)
    body = models.TextField(
        max_length=2000,
        blank=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
        related_query_name='reviews')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        related_query_name='reviews')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    rating = models.IntegerField(choices=ratings)

    def __str__(self):
        return self.title
