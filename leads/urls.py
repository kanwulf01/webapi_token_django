from rest_framework import routers
from .api import LeadAPI, UserAPI,LeadAPIView
from .viewsets import vistasUser
from knox import views as knox_views
from django.urls import path, include



urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/leads', LeadAPI.as_view()),
    path('api/auth/Verleads', LeadAPIView.as_view()),
    path('api/auth/usuarios', UserAPI.as_view())
   ]


