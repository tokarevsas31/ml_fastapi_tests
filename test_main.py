from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    '''Tests main route "/" availability'''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    '''Tests predict positive tone of the text'''
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    '''Tests predict negative tone of the text'''
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'
