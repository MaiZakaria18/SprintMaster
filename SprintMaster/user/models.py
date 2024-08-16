from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('jounior', 'jounior'),
        ('senior', 'senior'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    def __str__(self):
        return self.username


