from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
description = """
PredictorApp API helps you predict the correct emotional color of the text. 🚀
"""

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
