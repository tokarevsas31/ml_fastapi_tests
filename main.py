from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    text: str

class Items(BaseModel):
    texts: List[str]

app = FastAPI()
classifier = pipeline("sentiment-analysis")

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]

@app.post("/predict_multiple/")
def predict_multiple(items: Items):
    return [classifier(text)[0] for text in items.texts]
