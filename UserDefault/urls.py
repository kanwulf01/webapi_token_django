from rest_framework import routers
from .api import  RegisterAPI, UserUserAPI, UserProfileAPI, UserProfileAPI3, ShowUser
from knox import views as knox_views
from django.urls import path, include
from rest_framework import views
from .viewsets import UserProfileView, EmpleadoView, UsuariosTodos
from rest_framework import routers

'''
router = routers.SimpleRouter()
router.register('usuarios', UsuariosTodos)

urlpatterns = router.urls
'''


urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/UserProfile/', RegisterAPI.as_view()),
    path('api/auth/registraUser', UserProfileView),
    path('api/auth/Usuarios', UserProfileAPI3.as_view()),
    path('api/auth/userMedico', UserUserAPI.as_view()),
    path('api/auth/usuarios', ShowUser.as_view()),



    ]

