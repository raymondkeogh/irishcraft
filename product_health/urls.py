from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_health, name='product_health'),
]
