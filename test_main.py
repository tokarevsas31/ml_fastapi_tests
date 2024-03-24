from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Text analysis"}


def positive_prediction():
    response = client.post("/predict/",
                           json={"text": "I am a great fan of pizza"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def negative_prediction():
    response = client.post("/predict/",
                           json={"text": "I don't want to live in USA or europe"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'
