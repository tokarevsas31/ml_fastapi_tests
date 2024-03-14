from fastapi import APIRouter
from routers import sentiment

main_router = APIRouter(prefix='/api')
main_router.include_router(sentiment.router)
