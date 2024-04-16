from django.urls import path
from . import views
from students_courses.views import AddStudentsRetrieveIntoCourseView

urlpatterns = [
    path(
        "courses/",
        views.CourseView.as_view(),
    ),
    path(
        "courses/<uuid:course_id>/",
        views.CourseDetailView.as_view(),
    ),
    path(
        "courses/<uuid:course_id>/students/",
        AddStudentsRetrieveIntoCourseView.as_view()
    ),
]

