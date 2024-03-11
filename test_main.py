from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    """
    Test the main endpoint to ensure it returns a 200 status code and
    the expected JSON response.

    This test checks that the main endpoint ("/") returns a 200 status code,
    indicating a successful request.
    It also asserts that the JSON response matches the expected message
    "Hello World".

    Returns:
        None

    Raises:
        AssertionError: If the response status code is not 200 or if
        the JSON response does not match the expected message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    """
    Tests the "/predict/" endpoint for positive sentiment prediction.
    Sends a POST request with a positive text and asserts a 200 status code and
    'POSITIVE' label in the response.

    Returns:
        None

    Raises:
        AssertionError: If the status code is not 200 or the label
        is not 'POSITIVE'.
    """
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    """
    Tests the "/predict/" endpoint for negative sentiment prediction.
    Sends a POST request with a negative text and asserts a 200 status code and
    'NEGATIVE' label in the response.

    Returns:
        None

    Raises:
        AssertionError: If the status code is not 200 or the label
        is not 'NEGATIVE'.
    """
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'


def test_translate_en_ru_ok():
    """
    Tests the translation endpoint for English to Russian.

    This test sends a POST request to the "/translation_en_to_ru/" endpoint
    with the text "hello" and expects a 200
    status code and a JSON response containing the translated text "Привет."

    Returns:
        None

    Raises:
        AssertionError: If the status code is not 200 or the JSON response
        does not contain the expected translation text.
    """
    response = client.post(
        "/translation_en_to_ru/",
        json={"text": "hello"}
    )
    assert response.status_code == 200
    assert response.json() == {"translation_text": "Привет."}


def test_translate_en_ru_phrase_ok():
    """
    Tests the translation of English text to Russian.

    This test case sends a POST request to the "/translation_en_to_ru/"
    endpoint with an example English text. It then asserts that the response
    status code is 200 and that the returned translation text matches
    the expected Russian translation.

    Returns:
        None

    Raises:
        AssertionError: If the status code is not 200 or the JSON response
        does not contain the expected translation text.
    """
    response = client.post(
        "/translation_en_to_ru/",
        json={"text": "this is just an example text"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "translation_text": "Это всего лишь пример текста."}


def test_translate_en_ru_error():
    """
    Tests the translation of English text to Russian, expecting an error
    in translation.

    This test case sends a POST request to the "/translation_en_to_ru/"
    endpoint with the English word "hello". It then asserts that the response
    status code is 200 and that the returned translation text does not match
    the incorrect translation "Не Привет."

    Returns:
        None

    Raises:
        AssertionError: If the status code is not 200 or the JSON response
        matches the incorrect translation.
    """
    response = client.post(
        "/translation_en_to_ru/",
        json={"text": "hello"}
    )
    assert response.status_code == 200
    assert not response.json() == {"translation_text": "Не Привет."}


def test_translate_en_ru_error_not_200():
    """
    Tests the translation endpoint for handling errors, expecting a non-200
    status code.

    This test case sends a POST request to the "/translation_en_to_ru/"
    endpoint with an incorrect payload containing a "message" key instead of
    the expected "text" key. It then asserts that the response status code
    is 422, indicating a validation error.

    Returns:
        None

    Raises:
        AssertionError: If the status code is not 422, indicating that
        the endpoint did not handle the error as expected.
    """
    response = client.post(
        "/translation_en_to_ru/",
        json={"message": "hello"}
    )
    assert response.status_code == 422


def test_translation_ru_en_ok():
    """
    Tests the translation of Russian text to English.

    This test case sends a POST request to the "/translation_ru_to_en/"
    endpoint with the Russian word "привет". It then asserts that the response
    status code is 200 and that the returned translation text matches
    the expected English translation "Hey."

    Returns:
        None

    Raises:
        AssertionError: If the status code is not 200 or the JSON response
        does not contain the expected translation text.
    """
    response = client.post(
        "/translation_ru_to_en/",
        json={"text": "привет"}
    )
    assert response.status_code == 200
    assert response.json() == {"translation_text": "Hey."}


def test_translation_ru_en_phrase_ok():
    """
    Tests the translation of a Russian phrase to English.

    This test case sends a POST request to the "/translation_ru_to_en/"
    endpoint with the Russian phrase "Это всего лишь пример текста."
    It then asserts that the response status code is 200 and that the returned
    translation text matches the expected English translation
    "It's just an example of a text."

    Returns:
        None

    Raises:
        AssertionError: If the status code is not 200 or the JSON response
        does not contain the expected translation text.
    """
    response = client.post(
        "/translation_ru_to_en/",
        json={"text": "Это всего лишь пример текста."}
    )
    assert response.status_code == 200
    assert response.json() == {
        "translation_text": "It's just an example of a text."}


def test_translation_ru_en_error():
    """
    Tests the translation of Russian text to English, expecting an error
    in translation.

    This test case sends a POST request to the "/translation_ru_to_en/"
    endpoint with the Russian word "привет". It then asserts that the response
    status code is 200 and that the returned translation text does not match
    the incorrect translation "Hi."

    Returns:
        None

    Raises:
        AssertionError: If the status code is not 200 or the JSON response
        matches the incorrect translation.
    """
    response = client.post(
        "/translation_ru_to_en/",
        json={"text": "привет"}
    )
    assert response.status_code == 200
    assert not response.json() == {"translation_text": "Hi."}


def test_translation_ru_en_not_200():
    """
    Tests the translation endpoint for handling errors, expecting a non-200
    status code.

    This test case sends a POST request to the "/translation_ru_to_en/"
    endpoint with an incorrect payload containing a "message" key instead of
    the expected "text" key. It then asserts that the response status code
    is 422, indicating a validation error.

    Returns:
        None

    Raises:
        AssertionError: If the status code is not 422, indicating that
        the endpoint did not handle the error as expected.
    """
    response = client.post(
        "/translation_ru_to_en/",
        json={"message": "привет"}
    )
    assert response.status_code == 422
