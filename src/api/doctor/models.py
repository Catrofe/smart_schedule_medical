from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class DoctorRegister(BaseModel):
    fullName: str
    email: str
    phoneNumber: str


class DoctorOutput(DoctorRegister):
    id: int
    createdAt: datetime
    updateAt: Optional[datetime] = None


class DoctorEdit(BaseModel):
    email: str
    phoneNumber: str
    fullName: str