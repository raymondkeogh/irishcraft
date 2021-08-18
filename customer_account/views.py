from django.shortcuts import render

# Create your views here.


def customer_account(request):
    """A view that renders the users account"""

    return render(request, 'customer_account/customer_account.html')
