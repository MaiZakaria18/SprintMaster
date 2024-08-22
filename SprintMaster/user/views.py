from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework import status
from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db import IntegrityError
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny

# DRF API View for signup


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)

    if serializer.is_valid():
        try:
            serializer.save()
            return Response({'success': True, }, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in str(e):
                if 'user_customuser.username' in str(e):
                    return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
                elif 'user_customuser.email' in str(e):
                    return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'Error creating user. Please try again.'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = CustomUser(request, email=email, password=password)

        if user is not None:
            try:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            except InvalidToken:
                return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
