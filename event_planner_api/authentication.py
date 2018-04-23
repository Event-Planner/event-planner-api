from tokenapi.tokens import token_generator
from tokenapi.views import token_new

from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def authenticate_login(request):
    """
    Given a valid username and password, return an api token
    """
    return token_new(request)


def authenticate_request():
    """
    Validate username, token pair
    """
    raise NotImplementedError


def authenticate_fail():
    """
    Return an error message upon authentication failure
    """
    raise NotImplementedError
