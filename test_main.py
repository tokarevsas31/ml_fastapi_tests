from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_predict_positive():
    response = client.post("/predict/", json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["predict_result"]["label"] == "POSITIVE"


def test_predict_negative():
    response = client.post("/predict/", json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["predict_result"]["label"] == "NEGATIVE"
