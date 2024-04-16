"""
URL configuration for _core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     # path("api/users/", register_user, name="register_user"), 
#     path("api/", include("accounts.urls")),
#     path("api/", include("courses.urls")),
#     path("api/", include("contents.urls")),
#     path(
#         "api/docs/swagger-ui/",
#         SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",
#     ),
#     path(
#         "api/schema/",
#         SpectacularAPIView.as_view(),
#         name="schema"
#     ),
# ]


urlpatterns = [
    path("", RedirectView.as_view(url="/login/")),  # Redireciona a raiz para a página de login
    path("admin/", admin.site.urls),
    path("api/", include("accounts.urls")),
    path("api/", include("courses.urls")),
    path("api/", include("contents.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]