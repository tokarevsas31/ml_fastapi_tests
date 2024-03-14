from fastapi import FastAPI
from transformers import pipeline
from schemas import Item, Sentiment


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}


@app.post("/predict/", response_model=Sentiment)
def predict(item: Item) -> Sentiment:
    """
    Runs sentiment analysis on text
    """
    result = classifier(item.text)[0]
    return Sentiment(**result)
