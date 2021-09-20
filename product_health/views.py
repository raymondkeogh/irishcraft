
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.http import JsonResponse

from checkout.models import Order
from .models import ProductActivity, PurchaseHistory


@login_required
def product_health(request):
    """A view that renders products that are related to eachother by way of orders"""

    allorders = Order.objects.all()
    products = PurchaseHistory.objects.all()
    product_activity = ProductActivity.objects.all()
 

    template = 'product_health/product_health.html'
    context = {
        'allorders': allorders,
        'product_activity': product_activity,
        'products': products,
    }
    return render(request, template, context)


# https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html
def product_chart(request):
    labels = []
    data = []

    queryset = ProductActivity.objects.values('name__name').annotate(views=Sum('view_count')).order_by('-views')

    for entry in queryset:
        print(entry)
        labels.append(entry['name__name'][:15])
        data.append(entry['views'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
