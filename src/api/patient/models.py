from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PatientRegister(BaseModel):
    name: str
    email: str
    phoneNumber: str
    doctorId: int


class PatientUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phoneNumber: Optional[str]
    treated: Optional[bool]
    called: Optional[bool]
    doctorId: Optional[int]


class Patient(PatientRegister):
    id: int
    called: bool
    treated: bool
    createdAt: datetime
    updateAt: Optional[datetime]
