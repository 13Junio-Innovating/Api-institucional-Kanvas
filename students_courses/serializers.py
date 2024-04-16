from rest_framework import serializers
from accounts.models import Account
from rest_framework.response import Response
from rest_framework.views import status
from courses.models import Course
from .models import StudentCourse


class StudentCourseSerializer(serializers.ModelSerializer):
    student_id = serializers.UUIDField(
        read_only=True,
        source="student.id",
    )
    student_username = serializers.CharField(
        read_only=True,
        source="student.username",
    )
    student_email = serializers.EmailField(
        source="student.email",
    )

    class Meta:
        model = StudentCourse
        fields = [
            "id",
            "student_id",
            "student_username",
            "student_email",
            "status",
        ]
        read_only_fields=[
            "status"
        ]

class PutSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "students_courses"
        ]
        
        extra_kwargs= {
            "name": {"read_only": True}
        }


    def update(self, instance, validated_data):
        students = []
        not_found_students = []
        
        for student_course in validated_data.pop("students_courses"):
            student = student_course["student"]
            found_student = Account.objects.filter(email=student["email"]).first()
            if not found_student:
                not_found_students.append(student["email"])
            else:
                students.append(found_student)
        if not_found_students:
            raise serializers.ValidationError(
                {
                    "detail": f"No active accounts was found: {', '.join(not_found_students)}."
                }
            )
        if not self.partial:  
            instance.students.add(*students)
        return instance
