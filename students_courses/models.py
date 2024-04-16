from uuid import uuid4
from django.db import models


class Students_STATUS(models.TextChoices):
    pending = "pending"
    

class StudentCourse(models.Model):
    status = models.CharField(max_length=255, choices=Students_STATUS.choices, default=Students_STATUS.pending)
    student = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='students_courses')
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name='students_courses')
    id = models.UUIDField(default=uuid4, editable=False, unique=True, primary_key=True)