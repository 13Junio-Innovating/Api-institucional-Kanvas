from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import RetrieveUpdateAPIView
from accounts.permissions import IsAdmin
from courses.models import Course
from students_courses.serializers import PutSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import status
from rest_framework.response import Response


class AddStudentsRetrieveIntoCourseView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdmin]

    queryset = Course.objects.all()
    serializer_class = PutSerializer
    lookup_url_kwarg= "course_id"
