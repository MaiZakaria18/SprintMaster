from django.db import models
from project.models import Project
from user.models import CustomUser
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField()
    due_date = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return self.title
