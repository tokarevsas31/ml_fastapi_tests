[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.

Tests GitHub Actions

## Нow to launch the app

In the command line, go to the working folder and start the server by typing the code:

```
unicorn main:app
```

Next, in another command line, enter the curl command:

```
curl -X 'POST'
'http://127.0.0.1:8000/predict/'
-H 'accept: application/json'
-H 'Content-Type: application/json'
-d '{ "text": "I like machine learning!" }'
```
