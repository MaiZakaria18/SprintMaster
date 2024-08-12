from django.db import models
from task.models import Task
from user.models import CustomUser

class Attachment(models.Model):
    file = models.FileField()
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField()

    def __str__(self):
        return self.file
