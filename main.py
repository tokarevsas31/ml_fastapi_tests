from typing import Union
from typing import Optional
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    """
    Represents an item with a text attribute.
    """
    text: str

    def __str__(self):
        return f"Item(text={self.text})"

    def __repr__(self):
        return f"Item(text='{self.text}')"


class ResponseModel(BaseModel):
    """
    Represents a response model with a message.
    """
    message: Optional[str]


app = FastAPI()


@app.get("/")
def root() -> ResponseModel:
    """
    Returns a JSON object with a message "Hello World".

    :return: ResponseModel object with the message "Hello World"
    """
    return ResponseModel(message="Hello World")


@app.post("/predict/")
def predict(item: Item) -> Union[str, dict]:
    try:
        classifier = pipeline("sentiment-analysis")
        return classifier(item.text)[0]
    except Exception as e:
        return {"error": str(e)}
