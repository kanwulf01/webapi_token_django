from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer,UserSerializer, RegistraUserSerializer
from django.db import connection, transaction
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import UserHerenciaSerializer
from django.db import connection
from knox.models import AuthToken
from django.contrib.auth.models import User


#Lead Viewsets

class LeadAPI(generics.GenericAPIView):
    serializer_class = LeadSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lead = serializer.save()
        return Response({
            "lead":LeadSerializer(lead,context=self.get_serializer_context()).data,
            
     })



class LeadAPIView(APIView):

    def post(self,request, *args, **kwargs):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            lead = serializer.save()
            serializer = LeadSerializer(lead)
            return Response(serializer.data)
        
        return Response(serializer.errors)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserHerenciaSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })




class UserAPI(generics.RetrieveAPIView):

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
      
