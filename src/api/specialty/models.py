from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SpecialtyOutput(BaseModel):
    id: int
    name: str
    createdAt: datetime
    updateAt: Optional[datetime]


class SpecialtyInput(BaseModel):
    name: str = Field(min_length=3, max_length=255)
