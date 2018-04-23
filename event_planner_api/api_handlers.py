import json

from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from event_planner_api.authentication import authenticate_login, authenticate_request


@csrf_exempt
def get_token(request):
    """
    Given an http request, return a token
    """
    decoded_obj = decode_request(request)
    result = authenticate_login(decoded_obj)
    return return_json_response(result)


def decode_request(request):
    """
    Given an http request, return a dict object of the post parameters
    :param request: HTTP request obj
    :return: dict of post parameters
    """
    try:
        return json.loads(request.body.decode('utf-8'))
    except ValueError:
        raise ValidationError('Error decoding requets body')


def decode_and_authenticate_request(request):
    """
    Given an http request, decode dict obj and authenticate
    """
    raise NotImplementedError


def return_json_response(body, status=200):
    return HttpResponse(
        json.dumps(body),
        content_type='application_json',
        status=status
    )