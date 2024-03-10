"""
Модуль реализует API в приложении для классификации текста на предмет позитивного или негативного настроения.
"""
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
    Тестовое сообщение для проверки работоспособности"
    :return: текстовое сообщение - приветсвие
    """
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """
    Выполянет классификации текста на предмет
    позитивного или негативного настроения.
    :param item: Текстовая фраза для оценки
    :return: Возвращает словарь с результатом классификации текста.
    В ключе:
    "label" находится лейбл оценки, позитивная она или нет
    "score" находится оценка вероятности
    классификации текста этому лейблу
    """
    return classifier(item.text)[0]
