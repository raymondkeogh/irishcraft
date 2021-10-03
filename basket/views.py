"""
Basket App views
"""
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """A view to show the shopping basket"""
    return render(request, 'basket/basket.html')


# Elements from Code Institute boutique ado 'bag' tutorial
def add_to_basket(request, item_id):
    """A view to add a product to the basket"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})
    if quantity > 1:
        plural_string = "s"
    else:
        plural_string = ""
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request,
            f'Added {quantity} "{product.name}{plural_string}" to your basket')
    else:
        basket[item_id] = quantity
        messages.success(
            request,
            f'Added {quantity} "{product.name}{plural_string}" to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """A view to adjust the items in the basket"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request, f'Updated your basket item {product.name}')

    else:
        basket.pop[item_id]
        messages.success(
            request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove an item from the basket"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(
            request, f'{product.name} has been removed from your bag')
        request.session['basket'] = basket

        return HttpResponse(status=200)

    except Exception as err:
        messages.error(
            request, f'Error deleting item: {err}')
        return HttpResponse(status=500)
