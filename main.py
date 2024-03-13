from fastapi import FastAPI
import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast


app = FastAPI()
tokenizer = BertTokenizerFast.from_pretrained(
    "blanchefort/rubert-base-cased-sentiment"
)
model = AutoModelForSequenceClassification.from_pretrained(
    "blanchefort/rubert-base-cased-sentiment", return_dict=True
)
result = ["нейтральный", "позитивный :)", "негативный (("]


@app.get("/")
def root() -> dict:
    """
    This function works from root 
    and demonstrates welcome message.

    Returns:
        dict: Welcome message.
    """
    return {"message": "Hello World"}


@app.post("/predict/")
# функция для расчета модели,
# в "input" передаются текст
def predict(input: dict) -> dict:
    """
    This function predicts 

    Args:
        input (dict): dict with text for prediction
    
    Returns:
        dict: dict with the prediction of text sentiment
    """
    inputs = tokenizer(
        input["text"],
        max_length=512,
        padding=True,
        truncation=True,
        return_tensors="pt",
    )
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    predicted = torch.argmax(predicted, dim=1).numpy()
    output = {
        "Исходный текст": input["text"],
        "Результат:": result[int(predicted[0])],
    }  # формируем результат
    return output
