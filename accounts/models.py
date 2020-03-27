from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Medico(models.Model):

    tarjeta_medico = models.IntegerField()
    especialidades = models.CharField(max_length=200)
    user = models.OneToOneField(User, related_name="usuarios", on_delete=models.CASCADE)

