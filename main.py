from fastapi import FastAPI, Depends, HTTPException
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

def get_classifier():
    return pipeline("sentiment-analysis")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/predict/")
def predict(item: Item, classifier: pipeline = Depends(get_classifier)):
    try:
        result = classifier(item.text)[0]
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
