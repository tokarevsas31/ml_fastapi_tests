from fastapi import FastAPI

import src.handler.find_object as fo
import src.handler.classify_text as ct

app = FastAPI()


# метод приветствия для проверки работы сервера
@app.get("/")
async def healthcheck():
    return {'message': 'Hello World!!!'}


# метод поиска заданных объектов в картинке по ссылке
@app.post("/find-object/")
async def find_object(req: fo.Req):
    return fo.find_object(req)


# метод метод определения тональности текста
@app.post("/classify-text/")
def classify_text(req: ct.Req):
    return ct.classify_text(req)
