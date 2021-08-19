from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from customer_account.models import CustomerAccount

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    customer = get_object_or_404(CustomerAccount, user=request.user)

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'customer': customer,
        'stripe_public_key': ('pk_test_51JQ9rNIWHTiRInWXcHJzojA6w'
                              'x0mjdS6stINABnwChdlywr1WtMEwz1ZU'
                              'ZIiGlm6wkrWu2PyAYWhJyDMCuMawZNx00Ga5nBX2s'),
    }

    return render(request, template, context)
