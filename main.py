import argparse
import pathlib
import uuid
from contextlib import asynccontextmanager

import uvicorn
from databases import Database
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline


class Item(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    text: str
    label: str
    score: float


# Database connection configuration
DATABASE_URL = "sqlite+aiosqlite:///app_logs.db"
database = Database(DATABASE_URL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
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
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to initialize database: {e}"
        )
    yield
    # Disconnect from database on exit
    await database.disconnect()


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


app = FastAPI(lifespan=lifespan)


try:
    classifier = pipeline("sentiment-analysis")
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Model loading error: {e}")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
async def predict(item: Item):
    try:
        request_id = str(uuid.uuid4())
        prediction = classifier(item.text)[0]
    except Exception as e:  # Catching any unexpected errors during prediction
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
    values = {
        "id": request_id,
        "text": item.text,
        "label": prediction["label"],
        "score": prediction["score"],
    }
    query = "INSERT INTO predictions VALUES (:id, :text, :label, :score)"
    await database.execute(query=query, values=values)
    return values


@app.get("/predict/", response_model=PredictionResponse)
async def get_request(request_id: str):
    if not is_valid_uuid(request_id):
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid uuid matching a previous prediction",
        )
    values = {"request_id": request_id}
    query = "SELECT text, label, score FROM predictions WHERE id=:request_id"
    result = await database.fetch_one(query=query, values=values)
    if not result:
        raise HTTPException(
            status_code=404, detail="Provided uuid not found in previous predictions"
        )
    return PredictionResponse(**result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host IP address to bind the server",
    )
    args = parser.parse_args()
    cwd = pathlib.Path(__file__).parent.resolve()
    uvicorn.run(app, host=args.host, port=8000, log_config=f"{cwd}/log.ini")
