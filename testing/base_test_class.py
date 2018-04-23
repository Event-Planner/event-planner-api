import json
import mock
from tokenapi.tokens import token_generator

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'


class TestBaseTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin_user = load_user(ADMIN_USERNAME, ADMIN_PASSWORD, True, True, True)
        cls.admin_token = generate_token(ADMIN_USERNAME, ADMIN_PASSWORD)
        cls.client = Client()

    @staticmethod
    def create_user(username, password, is_active, is_staff, is_superuser):
        (instance, created) = User.objects.get_or_create(username=username)
        instance.set_password(password)
        instance.is_active = True
        instance.is_staff = True
        instance.is_superuser = True
        instance.save()
        return instance

    @staticmethod
    def generate_token(username, password):
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            return token_generator.make_token(user)
        return None
