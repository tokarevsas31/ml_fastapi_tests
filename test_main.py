from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    '''
    Тест на основной маршрут
    '''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "World"}


def test_predict_positive():
    '''
    Позитивный тест
    '''
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    '''
    Негативный тест
    '''
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'
