from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    with TestClient(app) as client:
        response = client.post("/predict/", json={"text": "I like machine learning!"})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data["label"] == "POSITIVE"


def test_predict_negative():
    with TestClient(app) as client:
        response = client.post("/predict/", json={"text": "I hate machine learning!"})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data["label"] == "NEGATIVE"
