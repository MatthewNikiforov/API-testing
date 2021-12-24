import requests
import pytest


@pytest.fixture
def total_users():
    url = 'https://reqres.in/api/users?page=1'
    response = requests.get(url)
    total_users = response.json()['total']
    yield total_users


@pytest.fixture
def total_pages():
    url = 'https://reqres.in/api/users?page=1'
    response = requests.get(url)
    total_pages = response.json()['total_pages']
    yield total_pages


@pytest.fixture
@pytest.mark.usefixtures('total_pages')
def all_ids(total_pages):
    list_of_all_ids = []
    for page in range(1, total_pages + 1):
        url = f'https://reqres.in/api/users?page={page}'
        response = requests.get(url)
        data = response.json()['data']
        for user in data:
            user_id = user['id']
            list_of_all_ids.append(user_id)
    yield list_of_all_ids


@pytest.fixture
def create_user_setup(request):
    url = 'https://reqres.in/api/users'
    user_data = {'email': 'exaple@mail.com',
                 'first_name': 'John',
                 'last_name': 'Smith'}
    request.cls.url = url
    request.cls.user_data = user_data
    yield


@pytest.fixture
def update_user_setup(request):
    url = 'https://reqres.in/api/users/1'
    user_data = {'email': 'exaple@mail.com',
                 'first_name': 'John',
                 'last_name': 'Smith'}
    request.cls.url = url
    request.cls.user_data = user_data
    yield


@pytest.fixture()
def registration_setup(request):
    url = 'https://reqres.in/api/register'
    correct_input = {"email": "eve.holt@reqres.in", "password": "pistol"}
    incorrect_input = {'email': 'incorrect@mail.com', 'password': 'incorrect'}
    request.cls.url = url
    request.cls.correct_input = correct_input
    request.cls.incorrect_input = incorrect_input
    yield


@pytest.fixture
def login_setup(request):
    url = 'https://reqres.in/api/login'
    correct_input = {"email": "eve.holt@reqres.in", "password": "pistol"}
    incorrect_input = {'email': 'incorrect@mail.com', 'password': 'incorrect'}
    request.cls.url = url
    request.cls.correct_input = correct_input
    request.cls.incorrect_input = incorrect_input
    yield
