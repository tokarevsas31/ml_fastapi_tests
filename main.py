from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """Sentiment analysis for a text

    Args:
        item (Item): have only attribute 'text' (str) for sentiment analysis

    Returns:
        dictionary: label (str): sentiment 'POSITIVE' or 'NEGATIVE'
                    score (float): accuracy assessment from 0 to 1
    """
    return classifier(item.text)[0]
