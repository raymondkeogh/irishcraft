from django.shortcuts import render
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    """ A view to return the index page """
    try:
        products = Product.objects.all()
        grid_sample_products = Product.objects.order_by('?')[:9]
    except ObjectDoesNotExist:
        products = None

    try:
        glassware_first = Product.objects.filter(
            category__name="glassware").first()
    except ObjectDoesNotExist:
        glassware_first = None

    try:
        textiles_first = Product.objects.filter(
            category__name="textiles").first()
    except ObjectDoesNotExist:
        textiles_first = None

    try:
        prints_first = Product.objects.filter(
            category__name="prints").first()
    except ObjectDoesNotExist:
        prints_first = None

    try:
        kitchen_first = Product.objects.filter(
            category__name="kitchen").first()
    except ObjectDoesNotExist:
        kitchen_first = None

    context = {
        'products': products,
        'grid_sample_products': grid_sample_products,
        'glassware_first': glassware_first,
        'textiles_first': textiles_first,
        'prints_first': prints_first,
        'kitchen_first': kitchen_first,
    }
    return render(request, 'home/index.html', context)
