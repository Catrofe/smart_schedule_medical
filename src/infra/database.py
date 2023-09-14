from __future__ import annotations

from datetime import datetime

from pydantic_sqlalchemy import sqlalchemy_to_pydantic  # type: ignore
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.utils.settings import Settings

settings = Settings()

Base = declarative_base()


def get_session_maker() -> sessionmaker[AsyncSession]:
    url = settings.db_prod if settings.environment is not None else settings.db_test
    engine = create_async_engine(
        url,
        echo=False,
    )
    return sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def create_database() -> None:
    url = settings.db_prod if settings.environment is not None else settings.db_test
    engine = create_async_engine(
        url,
        echo=False,
    )
    if settings.environment == "TEST":
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


class Doctor(Base):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, index=True)
    fullName = Column(String(255))
    email = Column(String(155), unique=True)
    phoneNumber = Column(String(20), unique=True)
    createdAt = Column(DateTime, default=datetime.now())
    updateAt = Column(DateTime, onupdate=datetime.now())

PydanticDoctor = sqlalchemy_to_pydantic(Doctor)
