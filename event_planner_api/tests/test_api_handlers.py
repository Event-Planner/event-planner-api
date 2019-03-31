import json

from django.http import HttpResponse
from testing.base_test_class import TestBase

from event_planner_api.api_handlers import (
    decode_request,
    decode_and_authenticate_request,
    get_token,
    return_json_response,
)


class TestApiHandlers(TestBase):
    def test_decode_request_correct(self):
        original_dict = {"string": "value", "int": 1, "bool": True}
        original_json = json.dumps(original_dict)
        request_object = self.factory.post(
            "/", data=original_json, content_type="application/json"
        )
        decoded_object = decode_request(request_object)

        self.assertEqual(decoded_object.get("string"), original_dict.get("string"))
        self.assertEqual(decoded_object.get("int"), original_dict.get("int"))
        self.assertEqual(decoded_object.get("bool"), original_dict.get("bool"))

    def test_return_json_response(self):
        response_body = {"string": "value", "int": 1, "bool": True}
        expected_json = json.dumps(response_body)
        expected_response = HttpResponse(
            expected_json, content_type="application_json", status=200
        )
        response = return_json_response(response_body)

        self.assertEqual(response.content, expected_response.content)
        self.assertEqual(response.status_code, expected_response.status_code)
        self.assertEqual(response.get("content_type"), response.get("content_type"))
