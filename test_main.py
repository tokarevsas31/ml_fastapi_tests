from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    """
    Тест проверяет корневой эндпоинт на корректность ответа и HTTP статуса.

    Ожидается, что ответ будет содержать приветственное сообщение и HTTP статус будет 200.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    """
    Тест проверяет эндпоинт анализа настроения на корректность обработки позитивного текста.

    Текст "I like machine learning!" выражает позитивное настроение, 
    поэтому ожидается, что ответ будет иметь метку 'POSITIVE' и HTTP статус 200.
    """
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    """
    Тест проверяет эндпоинт анализа настроения на корректность обработки негативного текста.

    Текст "I hate machine learning!" выражает негативное настроение, 
    поэтому ожидается, что ответ будет иметь метку 'NEGATIVE' и HTTP статус 200.
    """
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'
