import requests
import json
import pytest
from faker import Faker

@pytest.fixture()
def generate_user():
    fake=Faker('ru_RU') #будут сгенирированы русские пользователи
    return {
      "login": fake.user_name(),
      "email": fake.email(),
      "password": fake.password()
    }
@pytest.fixture()
def set_url():
    return "http://5.63.153.31:5051/v1/account"

@pytest.fixture()
def headers():
    return {
      'accept': '*/*',
      'Content-Type': 'application/json'
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

def test_post_v1_account(set_url, headers, generate_user):
    print(generate_user)
    response = requests.request("POST", set_url, headers=headers, json=generate_user)
    print(response.text)

@pytest.mark.parametrize('data0',data)
def test_post_v1_account_negative(set_url,headers,data0):
    print(data)
    response=requests.request("POST",set_url,headers=headers,json=data0)
    print(response.text)
