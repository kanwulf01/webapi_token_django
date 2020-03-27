from rest_framework import viewsets
from .models import UserProfile, Empleado
from .serializer import UserProfileSerializer, UserUserSerializer , EmpleadoSerializer, UserSerializer, UserUserSerializer
from django.contrib.auth.models import User

class UserProfileView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserUserSerializer

class EmpleadoView(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class UsuariosTodos(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserUserSerializer