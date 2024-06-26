from rest_framework import serializers
from .models import Course
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentCourseSerializer


class CourseSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(
        many=True,
        read_only=True,
    )
    students_courses = StudentCourseSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Course
        fields = [
            "id",
            "status",
            "name",
            "start_date",
            "end_date",
            "contents",
            "instructor",
            "students_courses",
        ]
        extra_kwargs = {
            "id": {"read_only": True},

            "instructor": {"required": False},
        }


class StudentSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(
        many=True,
    )
    name = serializers.CharField(
        read_only=True,
    )

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "students_courses",
        ]