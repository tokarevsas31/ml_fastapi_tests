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
    return classifier(item.text)[0]

en_ru_translator = pipeline("translation_en_to_ru", model="Helsinki-NLP/opus-mt-en-ru")
@app.post("/translation_en_to_ru/")
def predict(item: Item):
    return en_ru_translator(item.text)[0]