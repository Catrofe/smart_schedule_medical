import asyncio

import pytest
from fastapi.testclient import TestClient

from src.app import app, startup_event

client = TestClient(app)

URL_API = "/api/clinical/specialty/"


@pytest.fixture
def change_db_url():
    asyncio.run(startup_event())


def test_create_specialty_success(change_db_url):
    response = client.post(
        URL_API,
        json={
            "name": "Pediatria",
        },
    )
    assert response.status_code == 201
