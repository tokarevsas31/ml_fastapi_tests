from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
description = """
PredictorApp API helps you predict the correct emotional color of the text. 🚀
"""

description = """
PredictorApp API helps you predict the correct emotional color of the text.
## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_). 
"""


class Item(BaseModel):
    text: str


app = FastAPI(title="PredictorApp",
    description=description,
    summary="It will helps you",
    version="0.0.1",
)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]
