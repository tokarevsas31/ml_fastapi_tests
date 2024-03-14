from transformers import pipeline


# пайплайн с моделью
def get_text_classification():
    return pipeline("sentiment-analysis")
