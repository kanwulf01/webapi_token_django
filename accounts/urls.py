from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI
from rest_framework import routers
from knox import views as knox_views

'''
router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls
'''

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/users', UserAPI.as_view()),
]
