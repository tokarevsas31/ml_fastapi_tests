from fastapi import FastAPI, File, UploadFile
from transformers import pipeline
from pydantic import BaseModel
from pathlib import Path
from werkzeug.utils import secure_filename
import shutil
import os

UPLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = {".txt"}


class Item(BaseModel):
    text: str


app = FastAPI()


classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]


@app.post("/predict_from_file")
async def predict_from_file(upload_file: UploadFile = File(...)):
    """Uploads file and predicts text sentiment."""
    try:
        if not Path(upload_file.filename).suffix in ALLOWED_EXTENSIONS:
            return {
                "message": "Not allowed file format: only .txt is allowed."
            }
        filename = secure_filename(upload_file.filename)
        if not os.path.exists(UPLOAD_FOLDER):
            os.mkdir(UPLOAD_FOLDER)
        destination = Path(UPLOAD_FOLDER, filename)
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
        text = Path(destination).read_text()
        if os.path.exists(destination):
            os.remove(destination)
        return classifier(text)
    except Exception as e:
        return {"message": f"There was an error uploading the file:{str(e)}"}
    finally:
        upload_file.file.close()
