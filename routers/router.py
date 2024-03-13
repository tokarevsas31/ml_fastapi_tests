from fastapi import APIRouter
from transformers import pipeline
from shemas.shemas import Item


roure = APIRouter()
classifier = pipeline("sentiment-analysis")


@roure.get("/")
def root():
    return {"message": "Hello World"}


@roure.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]
