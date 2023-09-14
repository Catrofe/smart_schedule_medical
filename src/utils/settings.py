import os

from pydantic import BaseSettings

class Settings(BaseSettings):
    db_test: str = "sqlite+aiosqlite:///gym_test.db"
    db_prod: str = str(os.environ.get("URL_DATABASE"))
    environment: str = str(os.environ.get("ENVIRONMENT")) if os.environ.get("ENVIRONMENT") else "TEST"

    secret_key: str = (str(os.environ.get("GYM_ACCESS_TOKEN")))
    refresh_secret_key: str = (str(os.environ.get("GYM_REFRESH_TOKEN")))