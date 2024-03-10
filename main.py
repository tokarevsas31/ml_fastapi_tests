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
    Returns a greeting message "Hello World".

    Returns:
        dict:
        A dictionary with a key 'message' containing the string "Hello World".
    """
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """
    Predicts the classification of a given item using a trained classifier.

    Parameters:
        item (Item):
        An instance of the Item model containing the text to be classified.
    Returns:
        Any: The first element of the prediction result from the classifier.
    Example:
        { "text": "This is a sample text for prediction." }
    """
    return classifier(item.text)[0]


en_ru_translator = pipeline(
    task="translation_en_to_ru",
    model="Helsinki-NLP/opus-mt-en-ru"
)


@app.post("/translation_en_to_ru/")
def translate_en_to_ru(item: Item):
    """
   Translates English text to Russian using the Helsinki-NLP model.

   Parameters:
       item (Item):
       An instance of the Item model contains the English text
       to be translated.
   Returns:
       str: The translated Russian text.
   Example:
        { "text": "Hello, how are you?" }
   """
    return en_ru_translator(item.text)[0]


ru_en_translator = pipeline(
    task="translation_ru_to_en",
    model="Helsinki-NLP/opus-mt-ru-en"
)


@app.post("/translation_ru_to_en/")
def translate_ru_to_en(item: Item):
    """
    Translates Russian text to English using the Helsinki-NLP model.

    Parameters:
        item (Item):
        An instance of the Item model contains the Russian text
        to be translated.
    Returns:
        str: The translated English text.
    Example:
        { "text": "Привет, как дела?" }
    """
    return ru_en_translator(item.text)[0]
