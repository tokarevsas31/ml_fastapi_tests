from contextlib import asynccontextmanager
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from databases import Database
import uuid
# from local_db import db_init

# Database connection
database = Database("sqlite+aiosqlite:///requests.db")


class Item(BaseModel):
    text: str


class Request(BaseModel):
    id: str
    text: str
    prediction: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to database on start
    # db_init()
    await database.connect()
    create_table_query = '''
            CREATE TABLE IF NOT EXISTS requests
            (id TEXT PRIMARY KEY,
            text TEXT NOT NULL,
            prediction TEXT NOT NULL)
            '''
    await database.execute(query=create_table_query)
    query = "INSERT INTO requests(id, text, prediction) VALUES (:id, :text, :prediction)"
    values = {"id": "test_id", "text": "test_text", "prediction": "test_prediction"}
    await database.execute(query=query, values=values)
    yield
    # Disconnect from database on exit
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
classifier = pipeline("sentiment-analysis")

@app.post("/predict/")
async def predict(item: Item):
    request_id = str(uuid.uuid4())
    prediction = classifier(item.text)[0]

    query = "INSERT INTO requests(id, text, prediction) VALUES (:id, :text, :prediction)"
    values = {"id": request_id, "text": item.text, "prediction": str(prediction)}
    await database.execute(query=query, values=values)

    return {"id": request_id, "prediction": prediction}
