from uuid import uuid4
from django.db import models
from courses.models import Course

class Content(models.Model):
    name = models.CharField(max_length=150)
    content = models.TextField()
    video_url = models.URLField(max_length=200, null=True, blank=True)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name='contents')
    id = models.UUIDField(default=uuid4, editable=False, unique=True, primary_key=True)