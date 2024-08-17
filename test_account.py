import requests
import json
import pytest

@pytest.fixture()
def generate_user():
    return {
      "login": "login123456791",
      "email": "login1234567891@mail.ru",
      "password": "login1234567891"
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
    response = requests.request("POST", set_url, headers=headers, json=generate_user)
    print(response.text)

def test_post_v1_account2(set_url, headers, generate_user):
    response = requests.request("POST", set_url, headers=headers, json=generate_user)
    print(response.text)