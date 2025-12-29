import os
import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

import pytest

@pytest.fixture(scope="session")
def base_url():
    url = os.getenv("URL_FROM_TEST")
    if not url:
        raise ValueError("Переменная окружения URL_FROM_TEST не установлена!")
    return url.rstrip("/") + "/"


@pytest.fixture(scope="session")
def auth(base_url):
    payload = {
        "username": os.getenv("TEST_USERNAME", "IBA"),
        "password": os.getenv("TEST_PASSWORD", "IBA"),
        "code": os.getenv("TEST_CODE", "Xr6mQM"),
        "grant_type": "password",
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic YnJvd3NlcjoyYzlhNTA4MTc1NzM5YjFkMDE3NWI2NzAzZmU3MDAwNg==",
    }

    url = f"{base_url}user-service/oauth2/token"

    response = requests.post(url, data=payload, headers=headers, timeout=10, verify=False)

    if response.status_code != 200:
        raise AssertionError(f"Не удалось получить токен: {response.status_code}\n{response.text}")

    token = response.json().get("access_token")
    if not token:
        raise AssertionError("access_token не найден в ответе")

    return token