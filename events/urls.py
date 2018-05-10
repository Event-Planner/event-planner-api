from django.urls import path, include

from events.views import get_events

urlpatterns = [
    path('get_events/', get_events),
]