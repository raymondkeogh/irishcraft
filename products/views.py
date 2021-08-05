from django.shortcuts import render
from .models import Product, PhotoForm
from django.core.paginator import Paginator
from django.shortcuts import render


def upload(request):
    context = dict(backend_form=PhotoForm())

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'upload.html', context)


def all_products(request):
    """ A view to show all products """
    products = Product.objects.all()
    paginator = Paginator(products, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': products,
        'page_obj': page_obj,
    }

    return render(request, 'products/products.html', context)
    