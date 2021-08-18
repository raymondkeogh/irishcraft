from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomerAccount
from .forms import CustomerAccountForm
from checkout.models import Order


# Create your views here.

@login_required
def customer_account(request):
    """A view that renders the users account"""

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
    orders = customer.orders.all()

    template = 'customer_account/customer_account.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)
