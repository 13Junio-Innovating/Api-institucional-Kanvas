from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAdminAndAuthenticated
from .models import Content
from .serializers import ContentSerializer
from django.shortcuts import get_object_or_404
from courses.models import Course
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrStudentIsOwner
from rest_framework.exceptions import NotFound


class ContentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminAndAuthenticated]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        course_id = self.kwargs.get("course_id")

        obj_course = get_object_or_404(Course, id=course_id)

        serializer.save(course=obj_course)

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        return Content.objects.filter(course_id=self.kwargs.get("course_id"))


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsAuthenticated,
        IsAdminOrStudentIsOwner,
    ]

    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    lookup_url_kwarg = "content_id"

    def get_object(self):
        course_id = self.kwargs["course_id"]
        content_id = self.kwargs["content_id"]

        try:
            Course.objects.get(id=course_id)
            obj_content = Content.objects.get(id=content_id)
        except Course.DoesNotExist:
            raise NotFound(
                {"detail": "course not found."},
            )
        except Content.DoesNotExist:
            raise NotFound(
                {"detail": "content not found."},
            )

        self.check_object_permissions(
            self.request,
            obj_content,
        )
        return obj_content