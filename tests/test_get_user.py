import requests
import pytest


class TestGetUser:

    @pytest.mark.parametrize('page', ['1', '2', '100'])
    def test_get_users_list_status_code(self, page):
        url = f'https://reqres.in/api/users?page={page}'
        response = requests.get(url)
        assert response.status_code == 200

    @pytest.mark.usefixtures('total_users')
    def test_positive_get_single_user_status_code(self, total_users):
        url = f'https://reqres.in/api/users/{total_users}'
        response = requests.get(url)
        assert response.status_code == 200

    @pytest.mark.usefixtures('total_users')
    def test_negative_get_single_user_status_code(self, total_users):
        url = f'https://reqres.in/api/users/{total_users + 1}'
        response = requests.get(url)
        assert response.status_code == 404

    @pytest.mark.usefixtures('total_pages')
    def test_get_users_list_data(self, total_pages):
        url = f'https://reqres.in/api/users?page={total_pages}'
        response = requests.get(url)
        data = response.json()['data']
        assert len(data) > 0

    @pytest.mark.usefixtures('total_users')
    def test_single_user_data(self, total_users):
        url = f'https://reqres.in/api/users/{total_users}'
        response = requests.get(url)
        data = response.json()['data']
        assert tuple(data.keys()) == ('id', 'email', 'first_name', 'last_name', 'avatar')

    @pytest.mark.usefixtures('total_users')
    def test_single_user_data_types(self, total_users):
        url = f'https://reqres.in/api/users/{total_users}'
        response = requests.get(url)
        data = response.json()['data']
        data_types = tuple(map(type, data.values()))
        assert data_types == (int, str, str, str, str)
