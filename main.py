from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import uvicorn


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


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000)
