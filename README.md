[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.


On load in "/" API app, return message "Hello World'.

On request in "/predict/' using POST method, app predict text tone.
  - Input:
  -- JSON:
  --- text - string.
  - Output:
  -- JSON:
  --- label - string ("POSITIVE" || "NEGATIVE").
