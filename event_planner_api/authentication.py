from tokenapi.tokens import token_generator
from tokenapi.views import token_new

from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def authenticate_login(post_parameters):
    """
    Given a valid username and password, return an api token
    """
    username = post_parameters.get("username")
    password = post_parameters.get("password")
    if username and password:
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            return {"status": 0, "token": token_generator.make_token(user)}
        else:
            return {
                "status": 1,
                "error": "Unable to authenticate with credentials provided",
            }
    return {"status": 1, "error": "Must include username and password in request"}


def authenticate_request(post_parameters):
    """
    Validate username, token pair
    """
    username = post_parameters.get("username")
    token = post_parameters.get("token")

    if not username or not token:
        return False

    user = User.objects.filter(username=username).first()
    if user:
        if not user.is_active:
            return False
    else:
        return False

    return authenticate(pk=user, token=token)
