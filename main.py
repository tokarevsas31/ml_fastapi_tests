from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


# Определяем тип данных для входящего текста
class Item(BaseModel):
    text: str


# Создаем классификатор для анализа настроений с помощью pipeline
app = FastAPI()
classifier = pipeline("sentiment-analysis")


# Обработчик маршрута для запросов по корневому пути
# Возвращает текст "Hello World"
@app.get("/")
def root():
    return {"message": "Hello World"}


# Обработчик POST-запроса к модели
# Возвращает результат обработки модели
@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]
