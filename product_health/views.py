
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from checkout.models import Order
from .models import ProductActivity, PurchaseHistory


@login_required
def product_health(request):
    """A view that renders products that are related to eachother by way of orders"""

    allorders = Order.objects.all()
    product_activity = ProductActivity.objects.all()

    template = 'product_health/product_health.html'
    context = {
        'allorders': allorders,
        'product_activity': product_activity,
    }
    return render(request, template, context)
