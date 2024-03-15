import logging
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
