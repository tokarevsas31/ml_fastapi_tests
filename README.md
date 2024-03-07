# Sentiment Analysis API with FastAPI and Transformers

This repository contains code for a simple API built using FastAPI and Hugging Face's Transformers library to perform sentiment analysis on text inputs.

## Getting Started

To get started with this project, follow these instructions:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone this repository to your local machine:
  - git clone https://github.com/perfeus/ml_fastapi_tests.git
  - cd sentiment-analysis-api
  - pip install -r requirements.txt


### Usage

1. Start the FastAPI server:
  - uvicorn main:app --reload

2. Once the server is running, you can access the API at `http://localhost:8000`.

### Example

Use tools like cURL, Postman, or Python's `requests` library to interact with the API. Here's a `curl` example:

curl -X 'POST'
'http://127.0.0.1:8000/predict/'
-H 'accept: application/json'
-H 'Content-Type: application/json'
-d '{
"text": "This movie is fantastic!"
}'

This will return a JSON response with the predicted sentiment.

## API Endpoints

- `GET /`: Returns a simple "Hello World" message.
- `POST /predict/`: Performs sentiment analysis on the provided text input.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- [Hugging Face Transformers](https://huggingface.co/transformers/): State-of-the-art Natural Language Processing for PyTorch and TensorFlow 2.0.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
