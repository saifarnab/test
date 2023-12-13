"""
URL configuration for resend project.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    re_path(settings.STATIC_URL[1:] + r"(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("portal/", admin.site.urls),
    path("resend/", include('event.urls')),
]
