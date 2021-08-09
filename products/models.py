from django.db import models
from cloudinary.models import CloudinaryField
from django.forms import ModelForm      
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os


class Photo(models.Model):
  image = CloudinaryField('image')

class PhotoForm(ModelForm):
  class Meta:
    model = Photo
    fields = '__all__'


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField('image', default='No Image')

    def __str__(self):
        return self.name