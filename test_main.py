import uuid

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_read_main():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    with TestClient(app) as client:
        response = client.post("/predict/", json={"text": "I like machine learning!"})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data["label"] == "POSITIVE"


def test_predict_negative():
    with TestClient(app) as client:
        response = client.post("/predict/", json={"text": "I hate machine learning!"})
        json_data = response.json()
        assert response.status_code == 200
        assert json_data["label"] == "NEGATIVE"


def test_get_previous_prediction():
    # Posting a prediction request to ensure we have a known uuid to query
    with TestClient(app) as client:
        post_response = client.post(
            "/predict/", json={"text": "Neutral about technology."}
        )
        post_response_data = post_response.json()
        request_id = post_response_data["id"]

        # Testing GET with the uuid received from the post request
        get_response = client.get(f"/predict/?request_id={request_id}")
        json_data = get_response.json()
        assert get_response.status_code == 200
        assert json_data["text"] == "Neutral about technology."
        assert "label" in json_data and "score" in json_data


def test_get_prediction_invalid_uuid():
    # Testing GET with an invalid UUID
    with TestClient(app) as client:
        invalid_uuid = "this-is-not-a-valid-uuid"
        response = client.get(f"/predict/?request_id={invalid_uuid}")
        assert response.status_code == 400
        assert response.json() == {
            "detail": "Request query parameter 'request_id' must be a valid UUID."
        }


def test_get_prediction_not_found():
    # Generate a unique UUID for each test run
    non_existent_uuid = str(uuid.uuid4())  # Generate a new, random UUID

    with TestClient(app) as client:
        response = client.get(f"/predict/?request_id={non_existent_uuid}")
        assert response.status_code == 404
        assert response.json() == {
            "detail": "Provided uuid not found in previous predictions"
        }
