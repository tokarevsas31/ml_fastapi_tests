from transformers import pipeline

from src.model.text_classification import get_text_classification


def test_get_obj_detect_by_target():
    text_classification_pip = get_text_classification()
    assert text_classification_pip is not None
    assert isinstance(text_classification_pip, type(pipeline("sentiment-analysis")))
