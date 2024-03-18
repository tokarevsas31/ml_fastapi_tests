import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class Test_TestMain(unittest.TestCase):
    def test_read_main(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

    def test_predict_positive(self):
        response = client.post("/predict/", json={"text": "I like machine learning!"})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data["label"] == "POSITIVE"

    def test_predict_negative(self):
        response = client.post("/predict/", json={"text": "I hate machine learning!"})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data["label"] == "NEGATIVE"

    def test_predict_validation_error_empty(self):
        response = client.post("/predict/", json={"text": ""})
        assert response.status_code == 422

    def test_predict_validation_error_too_big_test(self):
        response = client.post("/predict/", json={"text": "abc" * 400})
        assert response.status_code == 422
