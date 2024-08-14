from django.urls import path
from .views import UserListView, UserDetailView, UserEditView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),  # List all users
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),  # View details of a specific user
    path('<int:pk>/edit/', UserEditView.as_view(), name='user_edit'),  # Edit a specific user's profile
]
