from fastapi.testclient import TestClient
import pytest


from main import app


@pytest.fixture
def client():
    test_client = TestClient(app)
    return test_client


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_websocket(client):
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "Hello WebSocket"}
