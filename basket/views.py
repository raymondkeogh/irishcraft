from django.shortcuts import render


def view_basket(request):
    """A view to show the shopping basket"""

    
    return render(request, 'basket/basket.html')