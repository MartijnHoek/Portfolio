import os

class Config:
    DEBUG = os.getenv("FLASK_ENV") == "development"