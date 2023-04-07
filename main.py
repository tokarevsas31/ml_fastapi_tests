from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import numpy as np


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")
score = np.array([])


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/average_score/")
def get_score():
    if len(score) == 0:
        return {"message": "There is no any score yet"}
    return {"requests": len(score), "mean": score.mean().round(4)}


@app.post("/predict/")
def predict(item: Item):
    global score
    score = np.append(score, classifier(item.text)[0].get('score'))
    return classifier(item.text)[0]
