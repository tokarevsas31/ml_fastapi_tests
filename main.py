from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str



app = FastAPI()
classifier = pipeline("sentiment-analysis")
en_fr_translator = pipeline("translation_en_to_fr")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]


@app.post("/translate/")
def translate(item: Item):
    return en_fr_translator(item.text)[0]
