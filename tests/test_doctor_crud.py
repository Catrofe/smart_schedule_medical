import asyncio

import pytest
from fastapi.testclient import TestClient

from src.app import app, startup_event

client = TestClient(app)

URL_API = "/api/clinical/doctors/"


@pytest.fixture
def change_db_url():
    asyncio.run(startup_event())


@pytest.fixture
def create_user(change_db_url):
    client.post(
        URL_API,
        json={
            "email": "teste@teste.com",
            "fullName": "Teste",
            "phoneNumber": "12345678901",
        },
    )


def test_register_new_doctor_success(change_db_url):
    response = client.post(
        URL_API,
        json={
            "email": "teste@teste.com",
            "fullName": "Teste",
            "phoneNumber": "12345678901",
        },
    )
    assert response.status_code == 201


def test_register_new_doctor_fail(create_user):
    response = client.post(
        URL_API,
        json={
            "email": "teste@teste.com",
            "fullName": "Teste",
            "phoneNumber": "12345678901",
        },
    )
    assert response.status_code == 409


def test_delete_doctor_success(create_user):
    response = client.delete("/api/clinical/doctors/1")
    assert response.status_code == 204


def test_delete_doctor_fail(create_user):
    response = client.delete(f"{URL_API}2")
    assert response.status_code == 400


def test_update_doctor_success(create_user):
    response = client.put(f"{URL_API}1", json={"email": "teste@123"})

    assert response.status_code == 200


def test_update_doctor_fail(create_user):
    response = client.put(f"{URL_API}2", json={"email": "teste@123"})

    assert response.status_code == 400


def test_get_doctor_by_id_success(create_user):
    response = client.get(f"{URL_API}1")
    assert response.status_code == 200


def test_get_doctor_by_id_fail(create_user):
    response = client.get(f"{URL_API}2")
    assert response.status_code == 400


def test_get_all_doctor_success(create_user):
    response = client.get(URL_API)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1
