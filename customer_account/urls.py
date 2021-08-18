from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_account, name='customer_account')
]
