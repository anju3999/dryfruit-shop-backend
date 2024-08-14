from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),  # List all orders
    path('<int:pk>/', views.order_detail, name='order_detail'),  # View details of a specific order
]
