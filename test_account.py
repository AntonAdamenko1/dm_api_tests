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

def test_post_v1_account(set_url, headers, generate_user):
    print(generate_user)
    response = requests.request("POST", set_url, headers=headers, json=generate_user)
    print(response.text)