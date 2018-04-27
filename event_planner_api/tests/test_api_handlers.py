import json

from testing.base_test_class import TestBase

from event_planner_api.api_handlers import decode_request, decode_and_authenticate_request, \
    get_token, return_json_response


class TestApiHandlers(TestBase):

    def test_decode_request_correct(self):
        original_dict = {
            'string': 'value',
            'int': 1,
            'bool': True,
        }
        original_json = json.dumps(original_dict)
        request_object = self.factory.post('/', data=original_json, content_type='application/json')
        decoded_object = decode_request(request_object)

        self.assertEqual(decoded_object.get('string'), original_dict.get('string'))
        self.assertEqual(decoded_object.get('int'), original_dict.get('int'))
        self.assertEqual(decoded_object.get('bool'), original_dict.get('bool'))

    def test_decode_request_type_error(self):
        original_dict = {
            'string': 'value',
            'int': 1,
            'bool': True,
        }
        original_json = json.dumps(original_dict)
        request_object = self.factory.post('/', data=original_json, content_type='application/json')
        self.assertRaises(TypeError, decode_request(request_object))
