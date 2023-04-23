from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    """Main endpoint for path. Return JSON object."""

    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """Endpoint for prediction text tonality"""

    return classifier(item.text)[0]
