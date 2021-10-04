"""
Customer Account views
"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from checkout.models import Order
from .models import CustomerAccount
from .forms import CustomerAccountForm


@login_required
def customer_account(request):
    """
    A view that renders the users account
    """
    customer = get_object_or_404(CustomerAccount, user=request.user)

    if request.method == 'POST':
        form = CustomerAccountForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated')
        else:
            messages.error(request,
                           'There"s a problem updating your account, Please'
                           'check to see all the fields are filled out'
                           'correctly')
    else:
        form = CustomerAccountForm(instance=customer)
    orders = customer.orders.order_by('-date')
    reviews = request.user.reviews.all()
    order_paginator = Paginator(orders, 4)
    page_number = request.GET.get('page')
    page_obj = order_paginator.get_page(page_number)

    template = 'customer_account/customer_account.html'
    context = {
        'form': form,
        'orders': orders,
        'customer': customer,
        'on_profile_page': True,
        'page_obj': page_obj,
        'reviews': reviews,
    }
    return render(request, template, context)


def edit_account(request):
    """
    A view to allow user to edit their account
    """
    customer = get_object_or_404(CustomerAccount, user=request.user)

    if request.method == 'POST':
        form = CustomerAccountForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details Saved')
        else:
            messages.error(request,
                           'There"s a problem saving your account details,'
                           'Please check to see all the fields are filled out'
                           'correctly')
        template = 'customer_account/customer_account.html'
        context = {'customer': customer, }
        return render(request, template, context)

    else:
        form = CustomerAccountForm(instance=customer)
    orders = customer.orders.all()

    template = 'customer_account/edit_account.html'
    context = {
        'form': form,
        'customer': customer,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def view_order(request, order_id):
    """
    A view that renders a chosen order
    """
    customer = get_object_or_404(CustomerAccount, user=request.user)
    order = get_object_or_404(Order, id=order_id)
    if request.user != order.customer_account.user:
        messages.error(
            request, "You cannot access this order"
            " unless logged in as the account owner"
            )
        return redirect(reverse('home'))

    template = 'customer_account/view_order.html'
    context = {
        'order': order,
        'customer': customer,
    }
    return render(request, template, context)
