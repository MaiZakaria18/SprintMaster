from django.db import models
from user.models import CustomUser
from task.models import Task

class Comment(models.Model):
    content = models.TextField(max_length=300)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
