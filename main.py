from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str



app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.on_event("startup")
def load_classifier():
    """
    Обработчик события запуска приложения.
    Загружает классификатор настроения приложения из библиотеки transformers.pipeline.
    """
    global classifier
    classifier = pipeline("sentiment-analysis")


@app.on_event("shutdown")
def close_classifier():
    """
    Обработчик события остановки приложения.
    Освобождает ресурсы, связанные с классификатором.
    """
    global classifier
    classifier = None


@app.get("/")
def root():
     """
    Обработчик для GET запроса на корневой URL.
    
    Returns:
        dict: Словарь с сообщением "Hello World".
    """
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """
    Обработчик для POST запроса на /predict/.
    
    Args:
        item (Item): Объект Item, содержащий текст для анализа настроения.
        
    Returns:
        dict: Словарь с предсказанием настроения текста.
    """
    return classifier(item.text)[0]
