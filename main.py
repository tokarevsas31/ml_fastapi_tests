from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import uvicorn


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


INFO = "An example of English text tone detection \
with [Hugging Face](https://huggingface.co/) library. \
Send POST /predict/YOU_PHRASE for tone detect"


@app.get("/")
def root():
    return {"message": INFO}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
