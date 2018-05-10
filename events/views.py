from event_planner_api.api_handlers import decode_and_authenticate_request, return_json_response

from events.event_api import search_for_events


@decode_and_authenticate_request
def get_events(request, decoded_request):

