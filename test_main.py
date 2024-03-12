from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# тест 1
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


# тест 2
def test_predict_positive():
    response = client.post("/predict/", json={"text": "I love you!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["Результат:"] == "позитивный :)"


# тест 3
def test_predict_negative():
    response = client.post("/predict/", json={"text": "I am very angry"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["Результат:"] == "негативный (("


# тест 4
def test_predict_russian_positive():
    response = client.post("/predict/", json={"text": "Я люблю учиться"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["Результат:"] == "позитивный :)"


# тест 5
def test_predict_russian_negative():
    response = client.post("/predict/", json={"text": "Я ненавижу тебя"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["Результат:"] == "негативный (("


# тест 6   
def test_predict_russian_neutral():
    response = client.post("/predict/", json={"text": "Сегодня наступила весна"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["Результат:"] == "нейтральный"


# тест 7
def test_predict_neutral():
    response = client.post("/predict/", json={"text": "Today spring has come"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["Результат:"] == "нейтральный"
