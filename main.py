import asyncio
import logging
import uvicorn

from sys import platform

from fastapi import FastAPI
from pydantic import BaseModel

import torch
from transformers import pipeline

# Define constants for application
APP_VERSION = "1.0.0"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Item model
class Item(BaseModel):
    text: str

default_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
default_host = "127.0.0.1" if platform == "win32" else "0.0.0.0"
default_port = 8000

# Define FastAPI app
app = FastAPI()

# Load NLP model for sentiment analysis
logger.info("Loading sentiment analysis model...")
classifier = pipeline("sentiment-analysis",
                      device=default_device,
                      framework="pt"
                      )
#classifier = pipeline("sentiment-analysis", framework="pt")
logger.info("Sentiment analysis model loaded successfully.")

# Define root endpoint
@app.get("/")
def root():
    return {"message": "Hello World"}

# Define predict endpoint
@app.post("/predict/")
async def predict(item: Item):
    try:
        logger.info("Received text for sentiment analysis: %s", item.text)
        result = await asyncio.to_thread(classifier, item.text)
        label = result[0]["label"]
        score = result[0]["score"]
        logger.info("Sentiment analysis result: label=%s, score=%f", label, score)
        return {"label": label, "score": score}
    except Exception as e:
        logger.error("Error during sentiment analysis: %s", e)
        return {"error": str(e)}

# Add version endpoint
@app.get("/version")
def version():
    return {"version": APP_VERSION}

# Warm start NLP model
@app.on_event("startup")
async def startup_event():
    logger.info("Warming up sentiment analysis model...")
    _ = await asyncio.to_thread(classifier, "This is a warm-up request")
    logger.info("Sentiment analysis model warmed up successfully.")

if __name__ == "__main__":
    uvicorn.run(
        app,
        port=default_port,
        host=default_host,
        log_level=logging.INFO,
        workers=1
    )