import json

from django.core.exceptions import ValidationError

from event_planner_api.authentication import authenticate_login, authenticate_request


def authenticate_request(request):
    """
    Given an http request, authenticate a user, token pair
    """
    raise NotImplementedError


def decode_request(request):
    """
    Given an http request, return a dict object of the post parameters
    :param request: HTTP request obj
    :return: dict of post parameters
    """
    try:
        return json.loads(request.body)
    except ValueError:
        raise ValidationError('Error decoding requets body')


def decode_and_authenticate_request(request):
    """
    Given an http request, decode dict obj and authenticate
    """
    raise NotImplementedError
