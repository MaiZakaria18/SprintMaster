from django.db import models
from django.conf import settings
from django.utils import timezone
from user.models import CustomUser


class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('Planned', 'Planned'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ])
    created_by = created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Ensure this is correct

    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.status}'
