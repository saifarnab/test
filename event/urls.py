from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import EventTrackerApiView

urlpatterns = [
    path("event", EventTrackerApiView.as_view(), name='event_tracker')
]

urlpatterns = format_suffix_patterns(urlpatterns)