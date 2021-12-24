import requests
import pytest


@pytest.mark.usefixtures('create_user_setup')
class TestCreateUserResponseBody:

    def test_create_user_status_code(self):
        response = requests.post(self.url, data=self.user_data)
        assert response.status_code == 201

    def test_create_user_body_keys(self):
        response = requests.post(self.url, data=self.user_data)
        response_json = response.json()
        assert ('email', 'first_name', 'last_name', 'id', 'createdAt') == tuple(response_json.keys())

    def test_create_user_body_values(self):
        response = requests.post(self.url, data=self.user_data)
        response_json = response.json()
        assert (self.user_data['email'], self.user_data['first_name'], self.user_data['last_name']) == \
               (response_json['email'], response_json['first_name'], response_json['last_name'])

    @pytest.mark.usefixtures('all_ids')
    def test_create_user_unique_id(self, all_ids):
        response = requests.post(self.url, data=self.user_data)
        assert response.json()['id'] not in all_ids
