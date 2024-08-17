from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import IntegrityError
from .models import CustomUser

# Serializer for CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)
        return user


# Serializer for Login
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise serializers.ValidationError('Invalid email or password.')
        else:
            raise serializers.ValidationError(
                'Email and password are required.')

        return data
