import os
import sys

from fastapi.testclient import TestClient

# так как запуск происходит из папки test, в sys.path добавляем её для импорта main
sys.path.append(os.path.join(os.getcwd()))
from main import app

client = TestClient(app)


def test_healthcheck_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World!!!'}


def test_find_object_car():
    response = client.post("/find-object/",
                           json={
                               "url": "https://parkingcars.ru/wp-content/uploads/2021/02/stoyanka-1024x683.jpg",
                               "targets": "car"
                           })
    json_data = response.json()

    assert response.status_code == 200
    assert len(json_data) == 12
    for res in json_data:
        assert res["label"] in ("car", "minivan")  # minivan нашло автоопределение


def test_find_object_pineapple():
    response = client.post("/find-object/",
                           json={
                               "url": "https://storage.yandexcloud.net/mfi/1242/products/main/3474.jpg",
                               "targets": "pineapple"
                           })
    json_data = response.json()

    assert response.status_code == 200
    assert len(json_data) == 2
    for res in json_data:
        assert res["label"] == "pineapple"


def test_classify_text_positive():
    response = client.post("/classify-text/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    response = client.post("/classify-text/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'
