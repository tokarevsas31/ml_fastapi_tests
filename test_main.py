from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_power():
    response = client.get("/power/?base=2&exp=3")
    assert response.status_code == 200
    assert response.json() == {"message":"2 to the power of 3 is 8."}


def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'
