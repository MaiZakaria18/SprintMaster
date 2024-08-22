from rest_framework import serializers
from .models import Task
from project.models import Project


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_title(self, value):
        # Check if a task with the same title already exists within the same project
        project = self.initial_data.get('project')
        if project and Task.objects.filter(title=value, project_id=project).exists():
            raise serializers.ValidationError(
                "A task with this title already exists within the same project.")
        return value

    def validate(self, data):
        # Ensure that the project is provided
        project = data.get('project')
        # Ensure that the project exists
        if not Project.objects.filter(id=project.id).exists():
            raise serializers.ValidationError(
                "The provided project does not exist.")

        # Ensure that the start_date is before the due_date
        if 'start_date' in data and 'due_date' in data:
            if data['start_date'] > data['due_date']:
                raise serializers.ValidationError(
                    "The start date must be before the due date.")

        return data
