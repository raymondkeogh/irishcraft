from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_health, name='product_health'),
    path('product-chart/', views.product_chart, name='product_chart'),
]
