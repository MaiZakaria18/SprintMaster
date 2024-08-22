from rest_framework import serializers
from .models import Project
from user.models import CustomUser
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


    def validate_name(self, value):
        if Project.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                "A project with this name already exists.")
        return value

    # Custom validation for the start date and end date
    def validate(self, data):
        if 'start_date' in data and 'end_date' in data:
            if data['start_date'] > data['end_date']:
                raise serializers.ValidationError(
                    "The start date must be before the end date.")
        return data


    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            print(f"Request user: {request.user}")
            if isinstance(request.user, CustomUser):
                print("The user is an instance of CustomUser.")
            else:
                print("The user is NOT an instance of CustomUser.")

        return super().create(validated_data)
