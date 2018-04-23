import json
from tokenapi.tokens import token_generator

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client


class TestBase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    @staticmethod
    def create_user(username, password, is_active=True, is_staff=False, is_superuser=False):
        (instance, created) = User.objects.get_or_create(username=username)
        instance.set_password(password)
        instance.is_active = is_active
        instance.is_staff = is_staff
        instance.is_superuser = is_superuser
        instance.save()
        return instance

    @staticmethod
    def generate_token(username, password):
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            return token_generator.make_token(user)
        return None

    @staticmethod
    def decode_response(response):
        return json.loads(response.content.decode('utf-8'))
