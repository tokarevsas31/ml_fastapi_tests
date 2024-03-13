from fastapi import FastAPI
from routers.router import roure


app = FastAPI(title="Models Ml")


app.include_router(roure)
