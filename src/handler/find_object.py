import requests
from PIL import Image
from pydantic import BaseModel
from tensorflow.keras.applications.efficientnet import decode_predictions
from ..model.obj_detect_auto import get_obj_detect_auto, preprocess_image
from ..model.obj_detect_by_target import get_obj_detect_by_target


# структура запроса
class Req(BaseModel):
    url: str
    targets: str


# загружаем модель для автоопределения
model_detect_auto = get_obj_detect_auto()

# инициализируем пайплайн с моделью для поиска по целям
model_detect_by_target = get_obj_detect_by_target()


def find_object(req: Req):
    image_obj = None

    # достаём изображение по ссылке
    if req.url:
        image_obj = Image.open(requests.get(req.url, stream=True).raw)

    obj_on_image = []

    if image_obj:
        # готовим изображение для автоопределения объектов
        pre_img = preprocess_image(image_obj)
        # определяем объекты
        preds = model_detect_auto.predict(pre_img)

        # берём 3 наиболее вероятных определения
        classes = decode_predictions(preds, top=3)[0]

        for cl in classes:
            # откидываем определения с маленькой вероятностью
            if cl[2] < 0.1:
                continue

            obj_on_image.append(cl[1])

    # подкидываем пользовательские цели для определения
    if req.targets:
        obj_on_image.extend(req.targets.split(", "))

    # убираем дубли
    obj_on_image = list(set(obj_on_image))

    # ищем в изображении объекты по указанным целям
    result = model_detect_by_target(
        image_obj,
        candidate_labels=obj_on_image,
    )

    # возвращаем результат
    return result
