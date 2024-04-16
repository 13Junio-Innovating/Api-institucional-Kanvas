from uuid import uuid4
from django.db import models


class COURSE_STATUS(models.TextChoices):
    not_started = "not started"
    in_progress = "in progress"
    finished = "finished"

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=11, choices=COURSE_STATUS.choices, default=COURSE_STATUS.not_started)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    instructor = models.ForeignKey("accounts.Account", on_delete=models.SET_NULL, null=True, related_name='courses')
    id = models.UUIDField(default=uuid4, editable=False, unique=True, primary_key=True)

    students = models.ManyToManyField("accounts.Account", through='students_courses.StudentCourse', related_name='my_courses')
