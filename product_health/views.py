"""Views for rendering data on product health"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Sum
from django.http import JsonResponse

from checkout.models import Order
from .models import ProductActivity


@login_required
def product_health(request):
    """
    A view that renders product activity data
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'You must have adminstrator access this area.')
        return redirect(reverse('home'))

    allorders = Order.objects.all()
    product_activity = ProductActivity.objects.all()

    template = 'product_health/product_health.html'
    context = {
        'allorders': allorders,
        'product_activity': product_activity,
    }
    return render(request, template, context)


# https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html
def product_chart(request):
    """
    View to hand json data to product_health template for chart rendering
    """
    labels = []
    data = []
    data2 = []

    queryset = ProductActivity.objects.values(
        'name__name', 'purchase_count').annotate(views=Sum(
            'view_count')).order_by('-views')
    for entry in queryset:
        labels.append(entry['name__name'])
        data.append(entry['views'])
        data2.append(entry['purchase_count'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
        'data2': data2,
    })
