# views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .forms import ProjectSerializer
from user.models import CustomUserManager
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
class ListProjects(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        projects = Project.objects.filter(created_by=request.models.CustomUserManager)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class AddProject(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save(commit=False)
            project.created_by = request.user
            project.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
