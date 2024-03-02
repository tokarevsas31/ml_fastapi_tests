[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.


Tests GitHub Actions

For startig Application you need give command:

uvicorn task_3_api_v2:app

For testing method GET of Application try:

curl -X 'GET' 'http://127.0.0.1:8000/'

For testing method POST try:

curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{ "text": "Эта лодка дырявая калоша."}'
