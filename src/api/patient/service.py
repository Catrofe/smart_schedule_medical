from fastapi import Request

from src.api.patient.models import PatientUpdate, PatientRegister
from src.api.patient.repository import PatientRepository


class PatientService:
    def __init__(self):
        self.repository = PatientRepository()

    async def create_patient(self, patient: PatientRegister, request: Request):
        patient = await self.repository.create_patient(patient, request)


    async def get_patients(self, request: Request):
        return await self.repository.get_patients(request)

    async def get_patient(self, patient_id: int, request: Request):
        return await self.repository.get_patient(patient_id, request)

    async def update_patient(self, patient_id: int, patient: PatientUpdate, request: Request):
        return await self.repository.update_patient(patient_id, patient, request)

    async def delete_patient(self, patient_id: int, request: Request):
        return await self.repository.delete_patient(patient_id, request)

