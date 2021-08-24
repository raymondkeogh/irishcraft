from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """
    products = Product.objects.all()
    grid_sample_products = Product.objects.order_by('?')[:9]

    glassware_first = Product.objects.filter(
        category__name="glassware").first()
    textiles_first = Product.objects.filter(
        category__name="textiles").first()
    prints_first = Product.objects.filter(
        category__name="prints").first()
    kitchen_first = Product.objects.filter(
        category__name="kitchen").first()

    context = {
        'products': products,
        'grid_sample_products': grid_sample_products,
        'glassware_first': glassware_first,
        'textiles_first': textiles_first,
        'prints_first': prints_first,
        'kitchen_first': kitchen_first,
    }
    return render(request, 'home/index.html', context)
