import requests
import pytest


class TestDeleteUser:

    @pytest.mark.usefixtures('total_users')
    def test_delete_user_status_code(self, total_users):
        url = f'https://reqres.in/api/users/{total_users}'
        response = requests.delete(url)
        assert response.status_code == 204
