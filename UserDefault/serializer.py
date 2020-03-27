from rest_framework import serializers
from .models import Empleado, UserProfile, UsuarioMedico
from django.contrib.auth.models import User


class EmpleadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleado
        fields = ("id","cargo")
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        allow_null = True
   
class MedicoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UsuarioMedico
        fields = ('id','numero','dependencia')

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    empleado = EmpleadoSerializer(many=False)
    
    class Meta:
        model = UserProfile
        fields = ('id','user','empleado')


    def create(self, validated_data):

        user = validated_data.pop('user')
        empleado = validated_data.pop('empleado')
        userprofile = UserProfile.objects.create(**validated_data)
        User.objects.create(userprofile=userprofile, **user)
        Empleado.objects.create(userprofile=userprofile, **empleado)
        return userprofile

class UserUserSerializer(serializers.ModelSerializer):
    usuario = MedicoSerializer(many=False)

    class Meta:
        model = User
        fields = ("id",'username','email','password','usuario')
        

    def create(self, validated_data):
        
        usuario = validated_data.pop('usuario')
        user = User.objects.create(**validated_data)
        UsuarioMedico.objects.create(user=user, **usuario)
        return user






