from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from transformers import pipeline


class Item(BaseModel):
    text: str

    @validator("text")
    def text_length_check(cls, value):
        if len(value) < 10:
            raise ValueError("Text must be at least 10 characters")
        return value


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]
