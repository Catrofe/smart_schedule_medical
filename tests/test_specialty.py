import asyncio

import pytest
from fastapi.testclient import TestClient

from src.app import app, startup_event

client = TestClient(app)

URL_API = "/api/clinical/specialty/"


@pytest.fixture
def change_db_url():
    asyncio.run(startup_event())


@pytest.fixture
def create_especialty(change_db_url):
    client.post(
        URL_API,
        json={
            "name": "Pediatria",
        },
    )


def test_create_specialty_success(change_db_url):
    response = client.post(
        URL_API,
        json={
            "name": "Pediatria",
        },
    )
    assert response.status_code == 201


def test_get_all_specialty_success(create_especialty):
    response = client.get(URL_API)
    assert response.status_code == 200
    assert response.json()[0].get("name") == "Pediatria"


def test_get_specialty_by_id_success(create_especialty):
    response = client.get(f"{URL_API}1/")
    assert response.status_code == 200
    assert response.json().get("name") == "Pediatria"


def test_get_specialty_by_id_not_found(create_especialty):
    response = client.get(f"{URL_API}2/")
    assert response.status_code == 404


def test_delete_specialty_success(create_especialty):
    response = client.delete(f"{URL_API}1/")
    assert response.status_code == 204


def test_delete_specialty_not_found(create_especialty):
    response = client.delete(f"{URL_API}2/")
    assert response.status_code == 404
