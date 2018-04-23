from tokenapi.tokens import token_generator
from tokenapi.views import token_new

from django.contrib.auth import authenticate


def authenticate_login(post_parameters):
    """
    Given a valid username and password, return an api token
    """
    username = post_parameters.get('username')
    password = post_parameters.get('password')
    if username and password:
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            return {
                'status': 0,
                'token': token_generator.make_token(user),
            }
        elif user and not user.is_active:
            return {
                'status': 1,
                'error': 'User is not active',
            }
        elif not user:
            return {
                'status': 1,
                'error': 'Unable to authenticate with credentials provided',
            }
    return {
        'status': 1,
        'error': 'Must include username and password in request',
    }


def authenticate_request(post_parameters):
    """
    Validate username, token pair
    """
    raise NotImplementedError
