from pydantic import BaseModel
from ..model.text_classification import get_text_classification


# структура запроса
class Req(BaseModel):
    text: str


# инициализируем пайплайн с моделью для классификации текста
model_classify = get_text_classification()


def classify_text(req: Req):
    return model_classify(req.text)[0]
