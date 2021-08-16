from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """A view to show the shopping basket"""
  
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """A view to add a product to the basket"""

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Added {product.name} to your bag')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """A view to adjust the items in the basket"""

    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop[item_id]

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove an item from the basket"""
    
    basket = request.session.get('basket', {})

    try:
        basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
