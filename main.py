from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel, Field
from predictor import Predictor


class Item(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=1024,
        description="text should have at least 1 symbol and at most 1024 symbols",
    )


predictor = Predictor()


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return predictor.predict(item.text)
