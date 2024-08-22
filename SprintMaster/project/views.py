from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    serializer = ProjectSerializer(
        data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_project(request, pk):
    try:
        project = Project.objects.get(pk=pk, created_by=request.user)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found or not owned by you.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProjectSerializer(
        project, data=request.data, partial=True, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_project(request, pk):
    try:
        project = Project.objects.get(pk=pk, created_by=request.user)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found or not owned by you.'}, status=status.HTTP_404_NOT_FOUND)

    project.delete()
    return Response({'message': 'Project deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
