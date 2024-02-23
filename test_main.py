from fastapi.testclient import TestClient
from main import app

# Создаем клиент для тестирования, передавая экземпляр FastAPI приложения
client = TestClient(app)


# Проверяем переход по корневому пути
# Ожидаемый результат: код 200 и содержание слова "world"
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "World"}


# Проверяем обработку предложения с позитивным эмоциональным окрасом
# Ожидаемый результат: код 200 и оценка POSITIVE
def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


# Проверяем обработку предложения с негативным эмоциональным окрасом
# Ожидаемый результат: код 200 и оценка NEGATIVE
def test_predict_negative():
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'
