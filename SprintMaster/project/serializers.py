from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'read_only': True},
        }

    def validate_name(self, value):
        if Project.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                "A project with this name already exists.")
        return value

    def validate(self, data):
        if 'start_date' in data and 'end_date':
            if data['start_date'] > data['end_date']:
                raise serializers.ValidationError(
                    "The start date must be before the end date.")
        return data

    def create(self, validated_data):
        # Automatically set the 'created_by' field to the authenticated user
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['created_by'] = request.user

        return super().create(validated_data)
