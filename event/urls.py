from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import EventTrackerApiView, unsubscribe_view

urlpatterns = [
    path("event", EventTrackerApiView.as_view(), name='event'),
    path("unsubscribe/<str:unsubscribe_token>", unsubscribe_view, name='unsubscribe')
]

urlpatterns = format_suffix_patterns(urlpatterns)