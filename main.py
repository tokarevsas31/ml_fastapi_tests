from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    """Главная страница проекта. Выводит сообщение Hello world."""
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """API-метод позволяет передать методом POST в модель sentiment-analysis
        текст и возвращает тональность переданного текста. """
    return classifier(item.text)[0]
