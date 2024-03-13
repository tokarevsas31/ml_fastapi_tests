from contextlib import asynccontextmanager
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from databases import Database
import uuid
import uvicorn
import pathlib


class Item(BaseModel):
    text: str


class Request(BaseModel):
    id: str
    text: str
    prediction: str


# Database connection
database = Database("sqlite+aiosqlite:///app_logs.db")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to database on start
    await database.connect()
    create_table_query = """
            CREATE TABLE IF NOT EXISTS predictions
            (id TEXT PRIMARY KEY,
            text TEXT NOT NULL,
            label TEXT NOT NULL,
            score REAL NOT NULL)
            """
    # Create requests table if it doesn't exist
    await database.execute(query=create_table_query)
    yield
    # Disconnect from database on exit
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
async def predict(item: Item):
    request_id = str(uuid.uuid4())

    prediction = classifier(item.text)[0]

    values = {"id": request_id, "text": item.text, "label": prediction["label"], "score": prediction["score"]}

    query = "INSERT INTO predictions VALUES (:id, :text, :label, :score)"

    await database.execute(query=query, values=values)

    return values


if __name__ == "__main__":
    cwd = pathlib.Path(__file__).parent.resolve()
    uvicorn.run(app, host="127.0.0.1", port=8000, log_config=f"{cwd}/log.ini")
