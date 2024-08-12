# forms.py
from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        today = timezone.now().date()

        if start_date and start_date < today:
            self.add_error('start_date', 'Start date cannot be in the past.')

        if end_date and end_date < today:
            self.add_error('end_date', 'End date cannot be in the past.')

        if start_date and end_date and end_date < start_date:
            self.add_error(
                'end_date', 'End date cannot be before the start date.')

        return cleaned_data
