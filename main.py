from fastapi import FastAPI, HTTPException
from transformers import pipeline
from pydantic import BaseModel, Field


class Item(BaseModel):
    text: str = Field(default="I loved Star Wars so much!",
                    title="Input text for sentiment analysis",
                    max_length=300)


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/",
          tags=["sentiment prediction"],
          summary="This method utilizes a pre-trained sentiment analysis model to predict the sentiment of a text sample you privede.",
          response_description="Prediction result"
          )
def predict(item: Item):
    if len(item.text)==0:
        raise HTTPException(status_code=404, detail="Item not found")
    result = classifier(item.text)
    return {"text": item.text, 
            "label": result[0]['label'], 
            "score": result[0]["score"]}

