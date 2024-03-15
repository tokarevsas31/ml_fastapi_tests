import logging
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Item(BaseModel):
    text: str



app = FastAPI()
classifier = pipeline("sentiment-analysis")



@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    # Добавлена обработка исключений
    try:
        prediction = classifier(item.text)[0]
        response = {
            "text": item.text,
            "sentiment": prediction["label"],
            "confidence_score": prediction["score"]
        }
        return response
    except Exception as e:
        logger.error(f"Prediction failed for input text: {item.text}. Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process the request")
