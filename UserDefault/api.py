from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializer import UserSerializer, UserProfileSerializer, UserUserSerializer
from django.db import connection, transaction
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from knox.models import AuthToken
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileAPI(generics.GenericAPIView):


   def post(self,request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            lead = serializer.save()
            serializer = UserProfileSerializer(lead)
            return Response(serializer.data)
        return Response(serializer.errors)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "userprofile":UserProfileSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user.user)[1],
        })


class UserUserAPI(generics.GenericAPIView):
    serializer_class = UserUserSerializer

    def post(self,request,*args, **kargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "User":UserUserSerializer(user, context=self.get_serializer_context()).data,
            "Token":AuthToken.objects.create(user)[1],
        })
 
class UserProfileAPI3(generics.ListCreateAPIView):
    queryset = User.objects.raw('select m.dependencia from auth_user a inner join "UserDefault_usuariomedico" m on  a.id = m.user_id')
    serializer_class = UserSerializer

class ShowUser(generics.GenericAPIView):


    def get_data():

        serializer_class = UserUserSerializer
        return Response({
            "User":UserUserSerializer(user, context=self.get_seriliazer_context()).data
        })
   