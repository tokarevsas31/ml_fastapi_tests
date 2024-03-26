from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]


@app.post("/predict/batch/")
def predict_batch(items: List[Item]):
    results = [classifier(item.text)[0] for item in items]
    return results
