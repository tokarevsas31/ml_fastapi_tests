from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    """
    Test the main endpoint to ensure it returns a 200 status code and the expected JSON response.

    This test checks that the main endpoint ("/") returns a 200 status code, indicating a successful request.
    It also asserts that the JSON response matches the expected message "World".
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    """
    Tests the "/predict/" endpoint for positive sentiment prediction.
    Sends a POST request with a positive text and asserts a 200 status code and 'POSITIVE' label in the response.

    Raises:
        AssertionError: If the status code is not 200 or the label is not 'POSITIVE'.
    """
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    """
    Tests the "/predict/" endpoint for negative sentiment prediction.
    Sends a POST request with a negative text and asserts a 200 status code and 'NEGATIVE' label in the response.

    Raises:
        AssertionError: If the status code is not 200 or the label is not 'NEGATIVE'.
    """
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'


def test_translate_en_ru_ok():
    response = client.post(
        "/translation_en_to_ru/",
        json={"text": "hello"}
    )
    assert response.status_code == 200
    assert response.json() == {"translation_text": "Привет."}


def test_translate_en_ru_phrase_ok():
    response = client.post(
        "/translation_en_to_ru/",
        json={"text": "this is just an example text"}
    )
    assert response.status_code == 200
    assert response.json() == {"translation_text": "Это всего лишь пример текста."}


def test_translate_en_ru_error():
    response = client.post(
        "/translation_en_to_ru/",
        json={"text": "hello"}
    )
    assert response.status_code == 200
    assert not response.json() == {"translation_text": "Не Привет."}


def test_translate_en_ru_error_not_200():
    response = client.post(
        "/translation_en_to_ru/",
        json={"message": "hello"}
    )
    assert response.status_code == 422


def test_translation_ru_en_ok():
    response = client.post(
        "/translation_ru_to_en/",
        json={"text": "привет"}
    )
    assert response.status_code == 200
    assert response.json() == {"translation_text": "Hey."}


def test_translation_ru_en_phrase_ok():
    response = client.post(
        "/translation_ru_to_en/",
        json={"text": "Это всего лишь пример текста."}
    )
    assert response.status_code == 200
    assert response.json() == {"translation_text": "It's just an example of a text."}


def test_translation_ru_en_error():
    response = client.post(
        "/translation_ru_to_en/",
        json={"text": "привет"}
    )
    assert response.status_code == 200
    assert not response.json() == {"translation_text": "Hi."}


def test_translation_ru_en_not_200():
    response = client.post(
        "/translation_ru_to_en/",
        json={"message": "привет"}
    )
    assert response.status_code == 422
