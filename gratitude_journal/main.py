from fastapi import FastAPI
# from gratitudejournal.core import config
from gratitude_journal.models.database import Base
from gratitude_journal.models.database import engine
# from gratitudejournal.routers.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


# def include_router(app):
#     app.include_router(api_router)


def start_application():
    app = FastAPI()
    create_tables()
    # include_router(app)
    return app


app = start_application()
