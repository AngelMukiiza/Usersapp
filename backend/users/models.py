from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Avoid related_name conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Change related_name to something unique
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Change related_name to something unique
        blank=True
    )
