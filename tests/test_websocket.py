from fastapi.testclient import TestClient
from app.main import app

def test_websocket_prediction():
    with TestClient(app) as client:
        with client.websocket_connect("/ws") as ws:
            landmarks = [0.5] * 63
            ws.send_json({"landmarks": landmarks})
            response = ws.receive_json()
            assert "letra" in response
            assert "confianza" in response
            assert 0 <= response["confianza"] <= 1

def test_websocket_invalid_format():
    with TestClient(app) as client:
        with client.websocket_connect("/ws") as ws:
            ws.send_text("no-json")
            response = ws.receive_json()
            assert "error" in response

def test_websocket_invalid_length():
    with TestClient(app) as client:
        with client.websocket_connect("/ws") as ws:
            ws.send_json({"landmarks": [0.5] * 10})
            response = ws.receive_json()
            assert "error" in response

def test_websocket_non_numeric():
    with TestClient(app) as client:
        with client.websocket_connect("/ws") as ws:
            landmarks = ["a"] * 63
            ws.send_json({"landmarks": landmarks})
            response = ws.receive_json()
            assert "error" in response
