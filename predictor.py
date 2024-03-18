from transformers import pipeline, Pipeline


class Predictor:
    classifier: Pipeline

    def __init__(self):
        self.classifier = pipeline("sentiment-analysis")

    def predict(self, text: str) -> str:
        res = self.classifier(text)

        return res[0]
