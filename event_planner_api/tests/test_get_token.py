from testing.base_test_class import TestBase


class TestGetToken(TestBase):

    def test_get_token_good(self):
        url = '/get_token/'
        username = self.admin_username
        password = self.admin_password

        post_data = {
            'username': username,
            'password': password,
        }
        response = self.send_json_post_request(url, post_data)
        response_body = self.decode_response(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_body.get('status'), 0)
        self.assertEqual(response_body.get('token'), self.admin_token)

    def test_get_token_inactive(self):
        url = '/get_token/'
        username = 'test@example.com'
        password = 'password'
        new_user = self.create_user(username, password, is_active=False)

        post_data = {
            'username': username,
            'password': password,
        }
        response = self.send_json_post_request(url, post_data)
        response_body = self.decode_response(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_body.get('status'), 1)
        self.assertEqual(response_body.get('error'), 'Unable to authenticate with credentials provided')

    def test_get_token_bad_credentials(self):
        url = '/get_token/'
        username = 'test@example.com'
        password = 'wrong_password'

        post_data = {
            'username': username,
            'password': 'wrong_password',
        }
        response = self.send_json_post_request(url, post_data)
        response_body = self.decode_response(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_body.get('status'), 1)
        self.assertEqual(response_body.get('error'), 'Unable to authenticate with credentials provided')

    def test_get_token_bad_request(self):
        url = '/get_token/'
        username = 'test@example.com'
        password = 'password'

        post_data = {
            'user': username,
            'pass': password,
        }
        response = self.send_json_post_request(url, post_data)
        response_body = self.decode_response(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_body.get('status'), 1)
        self.assertEqual(response_body.get('error'), 'Must include username and password in request')
