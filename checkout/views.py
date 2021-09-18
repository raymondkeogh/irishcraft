# From Code Institue Boutique Ado tutorial

from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from django.views.decorators.http import require_POST

from django.conf import settings

import stripe
import json

from basket.contexts import basket_contents
from django.core.exceptions import ObjectDoesNotExist

from customer_account.forms import CustomerAccountForm
from customer_account.models import CustomerAccount
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem, PurchaseHistory


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)



def checkout(request):
    """
    A view to show checkout data
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket"
                        " wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "There's nothing in \
                your basket at the moment")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info
        # the user has saved in their customer account
        if request.user.is_authenticated:
            try:
                customer = CustomerAccount.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': customer.user.get_full_name(),
                    'email': customer.user.email,
                    'phone_number': customer.phone_number,
                    'country': customer.country,
                    'postcode': customer.postcode,
                    'town_or_city': customer.town_or_city,
                    'street_address1': customer.street_address1,
                    'street_address2': customer.street_address2,
                    'county': customer.county,
                })
            except CustomerAccount.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        customer = CustomerAccount.objects.get(user=request.user)
       
        # Attach the user's profile to the order
        order.customer_account = customer
        order.save()
    
        # Save the user's info
        if save_info:
            customer_info = {
                'phone_number': order.phone_number,
                'town_or_city': order.town_or_city,
                'street_address1': order.street_address1,
                'street_address2': order.street_address2,
                'county': order.county,
                'country': order.country,
                'postcode': order.postcode,
            }
            customer_account_form = CustomerAccountForm(
                customer_info, instance=customer)
            if customer_account_form.is_valid():
                customer_account_form.save()

    for item in order.lineitems.all():
        # Connect lineitems to eachother in product_history object
        try:
            # check if item has a product history
            product_history = PurchaseHistory.objects.get(
                name__name=item.product)
            
        except ObjectDoesNotExist:
            product_history = None

        if product_history is not None:
            # attach the new product_history object to the order
            order.purchase_history = product_history
            order.save()
        else:
            # if there are no PurchaseHistory objects with the
            # item then create one
            product_history = PurchaseHistory.objects.create(
                name=item.product)
            order.purchase_history = product_history
            order.save()

    messages.success(request, f'Thank you for your order! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
