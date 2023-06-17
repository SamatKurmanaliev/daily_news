from django.shortcuts import render

from rest_framework import generics

from .models import User, Author
from .serializers import UserSerializer, AuthorSerializer


class AuthorRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer


class UserRegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
