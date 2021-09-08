from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_account, name='customer_account'),
    path('edit_account/', views.edit_account, name='edit_account'),
    path('<int:order_id>/', views.view_order, name='view_order'),
]
