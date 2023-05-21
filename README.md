[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.


Tests GitHub Actions

### Installation
To install the application, clone the repository and install the dependencies:

```commandline
git clone git@github.com:tokarevsas31/ml_fastapi_tests.git
cd ml_fastapi_tests
pip install -r requirements.txt
```


### Usage
To start the application, run the following command:

```commandline
uvicorn main:app
```
This will start the application at http://localhost:8000 or http://127.0.0.1:8000.

### API Documentation
The API documentation can be accessed at http://localhost:8000/docs (http://127.0.0.1:8000/docs).

### Docker
To run the application using Docker, first build the Docker image:
```commandline
docker build -t myapp .
```

Then run the Docker container:
```commandline
docker run -p 8000:8000 myapp
```

The application will be accessible at http://localhost:8000.

### Contributing
Contributions are welcome! Please feel free to submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.