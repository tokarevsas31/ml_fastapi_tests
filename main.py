from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    """
    Main page. Print "Hello World"
    """
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """
    The API method lets you send the POST method to the sentiment analysis model and returns the tone of the transmitted text.

    Args:
        item (Item)

    Returns:
        _type_: Tone of the text.
    """
    return classifier(item.text)[0]
