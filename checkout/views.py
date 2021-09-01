from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
import stripe
from basket.contexts import basket_contents
from django.core.exceptions import ObjectDoesNotExist

from customer_account.forms import CustomerAccountForm
from customer_account.models import CustomerAccount
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem, PurchaseHistory


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
                'country': order.country,
                'postcode': order.postcode,
                'town_or_city': order.town_or_city,
                'street_address1': order.street_address1,
                'street_address2': order.street_address2,
                'county': order.county,
            }
            customer_account_form = CustomerAccountForm(
                customer_info, instance=customer)
            if customer_account_form.is_valid():
                customer_account_form.save()

    for item in order.lineitems.all():
       
        # Attach the user's profile to the order

        try:
            product_history = PurchaseHistory.objects.get(name__name=item.product)
            print("youve got 1 exception ray")
        except ObjectDoesNotExist:
            product_history = None
            print("youve got an exception ray")

        if product_history is not None:
            product_history = PurchaseHistory.objects.get(name__name=item.product)
            
            order.purchase_history = product_history
            order.save()
            print("Product history :  - ", product_history)

        else:
            product_history = PurchaseHistory.objects.create(
                name=item.product)
            print("New Product history :  - ", product_history)
            order.purchase_history = product_history
            order.save()

       

        
        # p1 = Publication(title='The Python Journal')
        # purchase_history.save()
        # a1 = Article(headline='Django lets you build Web apps easily')
        # a1.save()
        # a1.publications.add(p1)

        # purchase_history1 = PurchaseHistory(product.set(item.product))
        # purchase_history1.save()
        # order.purchase_history.add(purchase_history)


        # order.purchase_history = purchase_history
        # order.save()


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
