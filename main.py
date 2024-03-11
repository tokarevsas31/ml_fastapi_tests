from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    """Handler for root method. For test only.

    Returns:
        str: response in JSON format
    """
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """Handler for /predict method.

    Args:
        item (Item): object with source text

    Returns:
        _type_: _description_
    """
    return classifier(item.text)[0]


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)
