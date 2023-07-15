import logging

from fastapi import FastAPI

from publisher.alerts.routers import router as alerts_router

api = FastAPI()

logging.basicConfig(level=logging.DEBUG)

@api.get("/")
def index():
    return {
        "service": "Weather Alert",
        "version": "v1",
        "docs_endpoint": "/redoc"
    }

api.include_router(alerts_router)