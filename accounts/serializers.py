from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Medico



class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('tarjeta_medico','especialidades')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class UserHerenciaSerializer(serializers.ModelSerializer):
    usuarios =  MedicoSerializer(many=False)
    class Meta:
        model = User
        fields = ('id','username', 'email','password','usuarios')
        extra_kwars = {'password':{'write_only':True}}


    def create(self, validated_data):
        usuario = validated_data.pop('usuarios')
        user = User.objects.create_user(**validated_data)
        Medico.objects.create(user=user, **usuario)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")