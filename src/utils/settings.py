import os

from pydantic import BaseSettings

class Settings(BaseSettings):
    db_test: str = "sqlite+aiosqlite:///gym_test.db"
    db_prod: str = str(os.environ.get("URL_DATABASE"))
    environment: str = str(os.environ.get("ENVIRONMENT")) if os.environ.get("ENVIRONMENT") else "TEST"
    internal_url: str = str(os.environ.get("INTERNAL_URL"))
