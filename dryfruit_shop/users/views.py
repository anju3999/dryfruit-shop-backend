from rest_framework import generics
from .models import User
from .serializers import UserSerializer  # Make sure this import is correct

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserEditView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
