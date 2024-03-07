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
async def score(text: str):
    html_content = f"<html><body><h1>Text Received:</h1><p>{text}</p></body></html>"
    return HTMLResponse(content=html_content)

print(classifier("I hate machine learning!"))