###Sentiment Analysis API
This is a simple API for performing sentiment analysis using the Hugging Face Transformers library and FastAPI.

###Installation
To install the dependencies, run:

```shell
pip install -r requirements.txt
```

###Running the server
To start the server, run:

```shell
uvicorn main:app --host 0.0.0.0 --port 8000
```
This will start the server at http://localhost:8000/.

###API endpoints
####GET /
Returns a JSON message:

```shell
{"message": "Hello World"}
```

####POST /predict/
Performs sentiment analysis on the input text and returns the predicted sentiment as a JSON object:

```shell
{
  "label": "POSITIVE",
  "score": 0.9998760223388672
}
```

###Example usage
You can use the following curl command to test the /predict endpoint:

```shell
curl -X POST "http://localhost:8000/predict/" -H "Content-Type: application/json" -d '{"text": "I love this product!"}'
```

This should return a JSON response with the predicted sentiment.
