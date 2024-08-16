from rest_framework import status
from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import IntegrityError
from .models import CustomUser
from .serializers import CustomUserSerializer
# DRF API View for signup


@api_view(['POST'])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)

    if serializer.is_valid():
        try:
            serializer.save()
            return Response({'success': True, 'redirect_url': '/login/'}, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in str(e):
                if 'user_customuser.username' in str(e):
                    return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
                elif 'user_customuser.email' in str(e):
                    return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'Error creating user. Please try again.'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data['email']
        user = authenticate(
            email=email, password=serializer.validated_data['password'])

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'redirect_url': '/list-project/'
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid email or password.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
