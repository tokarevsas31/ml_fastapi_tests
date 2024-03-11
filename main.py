from fastapi import FastAPI
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()

classifier = pipeline("sentiment-analysis")
tokenizer_en_ru = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
model_en_ru = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/"
                                                    "opus-mt-en-ru")


def translate_from_en(original_text):
    inputs = tokenizer_en_ru(original_text, return_tensors="pt")
    output = model_en_ru.generate(**inputs, max_new_tokens=100)
    out_text = tokenizer_en_ru.batch_decode(output, skip_special_tokens=True)
    return out_text[0]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]


@app.post("/en-ru/")
def translate_en_ru(item: Item):
    orig_text = item.text
    return translate_from_en(orig_text)
