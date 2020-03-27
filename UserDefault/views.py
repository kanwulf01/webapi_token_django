from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .serializer import UserSerializer, UserProfileSerializer
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.

class UserRetrieve(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

