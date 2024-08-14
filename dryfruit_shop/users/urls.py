from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),  # List all users
    path('<int:pk>/', views.user_detail, name='user_detail'),  # View details of a specific user
    path('<int:pk>/edit/', views.user_edit, name='user_edit'),  # Edit a specific user's profile
]
