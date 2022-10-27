from fastapi.testclient import TestClient
import pytest

from main import app


@pytest.fixture
def client():
    """Fixture to provide tests with a FASTApi test client"""
    test_client = TestClient(app)
    return test_client


def test_read_main(client):
    """Integration test for connection to the RESTApi endpoint of the server."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_websocket(client):
    """Integration test for connection to the websocket route."""
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "Hello WebSocket"}


@pytest.mark.parametrize("initial_expression, expected_result", [("3+1", '4.0')])
def test_evaluate(client, initial_expression, expected_result):
    """Integration test for evalute route of the websocket server."""
    with client.websocket_connect("/evaluate") as websocket:
        websocket.send_text(initial_expression)
        data = websocket.receive_json()
        assert data == {"result": expected_result}
