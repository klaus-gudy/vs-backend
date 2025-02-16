from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    CHOICES = [('admin', 'admin'), ('learner', 'learner'), ('instructor', 'instructor')]
    
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    role = models.CharField(max_length=20, choices=CHOICES, default='learner')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.username
