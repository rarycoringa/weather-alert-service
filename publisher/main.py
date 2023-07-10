from fastapi import FastAPI

from publisher.alerts.routers import router as alerts_router

api = FastAPI()

@api.get("/")
def index():
    return {"greeting": "hello"}

api.include_router(alerts_router)