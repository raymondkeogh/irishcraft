from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from customer_account.models import CustomerAccount
from basket.contexts import basket_contents
from django.conf import settings

from .forms import OrderForm

import stripe


def checkout(request):
    basket = request.session.get('basket', {})
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    order_form = OrderForm()
    if not stripe_public_key:
        messages.warning(request, 'Your stripe public key is missing,'
                         'did you set it in your environment?')
    customer = get_object_or_404(CustomerAccount, user=request.user)

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'customer': customer,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)
