from rest_framework import serializers
from leads.models import Lead
from django.contrib.auth import authenticate
from accounts.serializers import UserHerenciaSerializer
from django.contrib.auth.models import User

class RegistraUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email','password')
        extra_kwars = {"password":{"write_onlye":True}}

    def create(self, validated_data):
        usuario = User.objects.create_user(validated_data["username"],validated_data["email"],
        validated_data["password"])
        return usuario


#lead serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




class LeadSerializer(serializers.ModelSerializer):
    owner = UserHerenciaSerializer(many=False)
    class Meta:
        model = Lead
        fields = ('name','email','message','owner')

    def create(self, validated_data):
        owner = validated_data.pop('owner')
        lead = Lead.objects.create(**validated_data)
        User.objects.create(lead=lead, **owner)
        return lead



