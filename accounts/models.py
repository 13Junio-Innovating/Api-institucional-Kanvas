from uuid import uuid4  
from django.db import models
from django.contrib.auth.models import AbstractUser
from courses.models import Course

class Account(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid4, editable=False, unique=True, primary_key=True)
