from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


INFO = "An example of English text tone detection \
with [Hugging Face](https://huggingface.co/) library. \
Send POST /predict/YOU_PHRASE for tone detect"

POSITIVE_PHRASE = "I like machine learning!"
NEGATIVE_PHRASE = "I hate machine learning!"


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": INFO}


def test_predict_positive():
    response = client.post("/predict/", json={"text": POSITIVE_PHRASE})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "POSITIVE"


def test_predict_negative():
    response = client.post("/predict/", json={"text": NEGATIVE_PHRASE})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "NEGATIVE"
