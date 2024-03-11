from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis") # Setting sentinent-analysis pipeline


@app.get("/") # Adding GET method
def root():
    return {"message": "Hello World"}


@app.post("/predict/") # Adding POST method
def predict(item: Item):
    return classifier(item.text)[0]
