import requests
import json


def test_account():
    url = "http://5.63.153.31:5051/v1/account"

    payload = json.dumps({
      "login": "login123456791",
      "email": "login1234567891@mail.ru",
      "password": "login1234567891"
    })
    headers = {
      'accept': '*/*',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
