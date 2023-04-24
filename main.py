from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline(
    "sentiment-analysis",
    "blanchefort/rubert-base-cased-sentiment"
)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]
