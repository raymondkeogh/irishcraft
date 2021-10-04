""" Products view, handles image upload to cloudinary,
all products view and product details view """
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
from product_health.models import ProductActivity
from reviews.models import Review
from .forms import ProductForm
from .models import Product, PhotoForm


# https://cloudinary.com/documentation/django_image_and_video_upload
def upload(request):
    """ Connects to cloudinary to allow file upload"""
    context = dict(backend_form=PhotoForm())

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'upload.html', context)


# Products view altered from Code Institute Boutique Ado
def all_products(request):
    """ A view to show all products """
    products = Product.objects.all().order_by('name')
    query = None
    sort = None
    category = None
    direction = None
    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
            products = products.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    paginator = Paginator(products, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    current_sorting = f'{sort}_{direction}'
    on_product_page = True

    context = {
        'products': products,
        'page_obj': page_obj,
        'search': query,
        'category': category,
        'current_sorting': current_sorting,
        'on_product_page': on_product_page,
    }
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """
    A view to show products details
    """
    try:
        product = get_object_or_404(Product, id=product_id)
    except ObjectDoesNotExist:
        product = None

    # Check for product activity and update the ProductActivity model
    if product is not None:
        try:
            product_activity = ProductActivity.objects.get(
                name__name=product.name)
        except ObjectDoesNotExist:
            product_activity = None
        if product_activity is not None:
            product_activity.view_count = F(
                "view_count") + 1
            product_activity.save()
        else:
            product_activity = ProductActivity.objects.create(
                view_count=1,
                name=product,
            )

    try:
        reviews = Review.objects.filter(
                product=product.id).order_by('-created')
    except ObjectDoesNotExist:
        reviews = None

    review_paginator = Paginator(reviews, 4)
    page_number = request.GET.get('page')
    page_obj = review_paginator.get_page(page_number)

    context = {
        'product': product,
        'page_obj': page_obj,
        'reviews': reviews,
    }
    return render(request, 'products/product_details.html', context)


# Code Intitute Boutique Ado https://www.youtube.com/watch?v=bQuggmgIEEs
@login_required
def add_product(request):
    """
    upoad a product to the site
    """
    if not request.user.is_superuser:
        messages.error(
            request, "You must have shop Superuser access in order to"
            "add a product, please contact you web adminstrator in"
            "order to set up the correct permissions to access this function")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'{product.name} has been uploaded!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to upload product.'
                'Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Code Intitute Boutique Ado https://www.youtube.com/watch?v=0rRNZa7BR_Y
@login_required
def edit_product(request, product_id):
    """
    A view to edit product details
    """
    if not request.user.is_superuser:
        messages.error(request, 'You need to have the correct '
                       'permissions to edit product details, please contact'
                       ' you web administrator for more information')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'There was a problem updating.'
                           'the product, please check to see if all'
                           'the details have been filled in correctly')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    A view to delete a product from the database
    """
    if not request.user.is_superuser:
        messages.error(request, 'You need to have the correct '
                       'permissions to edit product details, please contact'
                       ' you web administrator for more information')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    product.delete()
    messages.success(request, f'{product.name} has been deleted!')
    return redirect(reverse('products'))
