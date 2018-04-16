from tokenapi.tokens import token_generator

from django.contrib.auth import authenticate


def authenticate_login():
    """
    Given a valid username and password, return an api token
    """
    raise NotImplementedError


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
