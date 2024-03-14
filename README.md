[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.  

**Main function**

Sentiment Analysis: Users can submit text for analysis, and the API returns the sentiment of the text using machine learning models.  

**Local installation instructions**

git clone git@github.com:tokarevsas31/ml_fastapi_tests.git  
pip install -r requirements.txt  
uvicorn main:app --reload  
