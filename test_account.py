import requests
import json
import pytest
from faker import Faker
from client import Client

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def generate_user():
    fake=Faker('ru_RU') #будут сгенирированы русские пользователи
    return {
      "login": fake.user_name(),
      "email": fake.email(),
      "password": fake.password()
    }

data=[
    # короткий логин
    {
        "login": "l",
        "email": "email_12345@mail.ru",
        "password": "12345678"
    },
    # невалидный емайл
    {
        "login": "login_12345678902",
        "email": "e",
        "password": "12345678"
    },
    # короткий пароль
    {
        "login": "login_12345678902",
        "email": "email_12345@mail.ru",
        "password": "1"
    }
]

@pytest.mark.parametrize('data',data)
def test_post_v1_account(data,client):
    response=client.register_user(data)
