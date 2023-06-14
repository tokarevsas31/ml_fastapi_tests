from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    """
    Корневой эндпоинт API.
    
    Возвращает:
        Словарь с приветственным сообщением.
    """
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """
    Эндпоинт для анализа настроения списка текстов.
    
    Аргументы:
        item (Item): Объект, содержащий список текстов для анализа настроения.
        
    Возвращает:
        Список результатов анализа настроения для каждого текста.
    """
    return classifier(item.text)[0]
