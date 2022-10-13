from fastapi import FastAPI
from src.db.base import Base
from src.db.session import engine
from fastapi.staticfiles import StaticFiles
from core.config import settings
import os
from src.routes.base import api_router

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def include_router(application):
    application.include_router(api_router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def configure_static(application):
    application.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, 'static')), name="static")


def start_application():
    apps = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(apps)
    create_tables()
    configure_static(apps)
    return apps


app = start_application()
