
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from checkout.models import Order


@login_required
def product_health(request):
    """A view that renders the users account"""

    allorders = Order.objects.all()

    template = 'product_health/product_health.html'
    context = {
        'allorders': allorders,
    }
    return render(request, template, context)
