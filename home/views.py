import random
from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """
    products = Product.objects.all()
    grid_sample_products = Product.objects.order_by('?')[:9]
    context = {
        'products': products,
        'grid_sample_products': grid_sample_products,
    }
    return render(request, 'home/index.html', context)
