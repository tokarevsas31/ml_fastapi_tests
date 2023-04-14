from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

HTTP_200_OK = 200

def test_read_main():
    try:
        response = client.get("/")
        assert response.status_code == HTTP_200_OK
        assert response.json() == {"message": "Hello World"}
    except AssertionError as e:
        print(e)
        assert False
    except Exception as e:
        print(e)
        assert False

def test_predict_positive():
    try:
        response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
        json_data = response.json()
        assert response.status_code == HTTP_200_OK
        assert json_data["label"] == "POSITIVE"
    except AssertionError as e:
        print(e)
        assert False
    except Exception as e:
        print(e)
        assert False

def test_predict_negative():
    try:
        response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
        json_data = response.json()
        assert response.status_code == HTTP_200_OK
        assert json_data["label"] == "NEGATIVE"
    except AssertionError as e:
        print(e)
        assert False
    except Exception as e:
        print(e)
        assert False