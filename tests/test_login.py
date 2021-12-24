import requests
import pytest


@pytest.mark.usefixtures('login_setup')
class TestLogIn:

    def test_login_status_code(self):
        expected_status_codes = (requests.post(self.url, data=self.correct_input).status_code,
                                 requests.post(self.url, data=self.incorrect_input).status_code)
        assert expected_status_codes == (200, 400)

    def test_positive_login(self):
        response = requests.post(self.url, data=self.correct_input)
        assert response.json() == {'token': 'QpwL5tke4Pnpja7X4'}

    def test_negative_login(self):
        response = requests.post(self.url, data=self.incorrect_input)
        assert response.json() == {'error': 'user not found'}

    def test_missing_email(self):
        response = requests.post(self.url, data={'password': self.correct_input['password']})
        assert response.json() == {'error': 'Missing email or username'}

    def test_missing_password(self):
        response = requests.post(self.url, data={'email': self.correct_input['email']})
        assert response.json() == {'error': 'Missing password'}
