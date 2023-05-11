from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


class Item(BaseModel):
    text: str


class PredictResponse(BaseModel):
    predict_result: dict


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.post(
    "/predict/",
    response_model=PredictResponse,
)
def predict(item: Item):
    return {"predict_result": classifier(item.text)[0]}
