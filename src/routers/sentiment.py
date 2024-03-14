from fastapi import APIRouter, Depends
from schemas.sentiment import Item, Sentiment
from services.sentiment import SentimentService, get_sentiment_service

router = APIRouter(prefix="/predict")


@router.post("", response_model=Sentiment)
def predict(
        item: Item,
        sentiment_service: SentimentService = Depends(get_sentiment_service)
) -> Sentiment:
    """
    Runs sentiment analysis on text and returns a scored sentiment
    (POSITIVE or NEGATIVE).
    """
    result = sentiment_service.process_text(item.text)
    return Sentiment(**result)
