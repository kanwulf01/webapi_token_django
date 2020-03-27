from django.db import models
from django.contrib.auth.models import User

# Create your models here.


'''
Clase principal
'''

class Empleado(models.Model):

    cargo = models.CharField(max_length=100)
    division = models.CharField(max_length=200)

    def __str__(self):
        return self.id


class UserProfile(models.Model):
    
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, related_name="empleado",on_delete=models.CASCADE )

    def __str__(self):
        return self.id


class UsuarioMedico(models.Model):
    numero = models.CharField(max_length=100)
    dependencia = models.CharField(max_length=200)
    user = models.OneToOneField(User, related_name="usuario", on_delete=models.CASCADE, null=True)
    





