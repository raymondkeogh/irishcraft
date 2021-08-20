import random
from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """
    num_products = Product.objects.all().count()
    rand_products = random.sample(range(num_products), num_products)
    sample_products = Product.objects.filter(id__in=rand_products)
   





   for i in range(y):
    string = ''.join([random.choice(x) for _ in range(v)])


    add_product_products = random.sample(
        range(num_products), 9)
    add_product_sample_products = (
        Product.objects.filter(id__in=add_product_products))
    context = {
        'random_product': sample_products,
        'add_product_sample_products': add_product_sample_products,
    }
    return render(request, 'home/index.html', context)

