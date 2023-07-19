from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    password2 = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    class Meta:
        model = User
        fields = ('username' , 'password1' , "password2")

    def create( self,validated_date):
        user = User(
            username = validated_date.get('username')
        )
        user.set_password(validated_date.get('password1'))
        user.save()
        return user

    def validate(self,data):
        data = super().validate(data)
        if data['password1'] != data['password2']:
            return self.ValidationError("Passwords do not match.")
        return data
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['username'] = self.user.username
        return data