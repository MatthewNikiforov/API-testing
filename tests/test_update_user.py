import requests
import pytest


@pytest.mark.usefixtures('update_user_setup')
class TestUpdateUserResponseBody:

    def test_update_user_status_code(self):
        response = requests.put(self.url, data=self.user_data)
        assert response.status_code == 200

    def test_update_user_body_keys(self):
        response = requests.put(self.url, data=self.user_data)
        response_json = response.json()
        assert ('email', 'first_name', 'last_name', 'updatedAt') == tuple(response_json.keys())

    def test_update_user_body_values(self):
        response = requests.put(self.url, data=self.user_data)
        response_json = response.json()
        assert (self.user_data['email'], self.user_data['first_name'], self.user_data['last_name']) == \
               (response_json['email'], response_json['first_name'], response_json['last_name'])
