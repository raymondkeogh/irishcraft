"""
Products, Category and photoform models
"""
from django.db import models
from django.forms import ModelForm

from cloudinary.models import CloudinaryField


class Photo(models.Model):
    """
    Cloudinary Image model
    """
    image = CloudinaryField('image')


class PhotoForm(ModelForm):
    """
    Photo form model
    """
    class Meta:
        model = Photo
        fields = '__all__'


class Category(models.Model):
    """
    Category model
    """
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(
        max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Return category friendly names
        """
        return self.friendly_name


# Modified Product Class from Code Institue Boutique Ado tutorial
class Product(models.Model):
    """
    Product Model
    """
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254,
        blank=True)
    name = models.CharField(
        max_length=254)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)
    image_url = models.URLField(
        max_length=1024,
        blank=True)
    image = CloudinaryField(
        'image',
        default='No Image',
        transformation={
            "quality": "auto:best"},
        format="jpg")

    def __str__(self):
        return self.name
