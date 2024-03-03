from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


# Проверка типа данных
class Item(BaseModel):
    text: str


# Создание классификатора для анализа тональности текста
app = FastAPI()
classifier = pipeline("sentiment-analysis")


# Возвращает текст "Hello World"
@app.get("/")
def root():
    return {"message": "Hello World"}


# Обработка POST-запроса и возвращение результата/ответа после обработки
@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]
