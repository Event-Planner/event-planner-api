from datetime import datetime

from cloud.models import Event, EventDescription, EventLocation, User, UserEventRole, UserProfile


def get_events(event_name=None):
    """
    Return events that have not started yet
    :param event_name: (str | event_name) event_name to query for
    :return: (QuerySet) Query set of events that match the user's query
    """
    time_now = datetime.now()
    events = Event.objects.filter(start_time__gt=time_now)
    if event_name:
        events = events.filter(name__icontains=name)

    return events
