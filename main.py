from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict/")
async def predict(item: Item):
    return classifier(item.text)[0]


@app.get("/power/")
async def power(base: int = 1, exp: int = 1):
    power = base ** exp
    # power_str = str(base)
    #             + " to the power of "
    #             + str(exp)
    #             + " is "
    #             + str(power)
    power_str = f"{base} to the power of {exp} is {power}."
    return {"message": power_str}
