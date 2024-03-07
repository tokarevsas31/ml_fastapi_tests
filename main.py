from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from fastapi.responses import HTMLResponse


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]


@app.post("/score/")
def score(item: Item):
    return classifier(item.text)[0]['score']
