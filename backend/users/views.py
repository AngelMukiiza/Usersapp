from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser  # Corrected import to CustomUser
from .serializers import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer