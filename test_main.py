from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "I love this day!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "POSITIVE"


def test_predict_negative():
    response = client.post("/predict/",
                           json={"text": "I don't love this day!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "NEGATIVE"


def test_predict_neutral():
    response = client.post("/predict/",
                           json={"text": "Sky"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "NEUTRAL"
