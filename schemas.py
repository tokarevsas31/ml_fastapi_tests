from pydantic import BaseModel


class Item(BaseModel):
    text: str


class Sentiment(BaseModel):
    label: str
    score: float
