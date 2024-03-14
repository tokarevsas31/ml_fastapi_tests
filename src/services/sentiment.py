from functools import lru_cache

from transformers import pipeline

from schemas.sentiment import Sentiment


class SentimentService:
    def __init__(self):
        self.classifier = pipeline(
            "sentiment-analysis",
            "distilbert/distilbert-base-uncased-finetuned-sst-2-english")

    def process_text(self, text) -> Sentiment:
        result = self.classifier(text)[0]
        return result


@lru_cache
def get_sentiment_service() -> SentimentService:
    return SentimentService()
