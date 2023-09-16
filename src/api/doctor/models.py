from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DoctorRegister(BaseModel):
    fullName: str
    email: str
    phoneNumber: str


class DoctorOutput(DoctorRegister):
    id: int
    createdAt: datetime
    updateAt: Optional[datetime] = None


class DoctorEdit(BaseModel):
    email: Optional[str]
    phoneNumber: Optional[str]
    fullName: Optional[str]
