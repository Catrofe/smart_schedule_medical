from fastapi import APIRouter, Request

from src.api.patient.models import PatientRegister, PatientUpdate
from src.api.patient.service import PatientService

service = PatientService()

router = APIRouter()


@router.post("/patient", status_code=201, response_model=PatientRegister)
async def create_patient(patient: PatientRegister, request: Request):
    return await service.create_patient(patient, request)


@router.get("/patient", status_code=200)
async def get_patients(request: Request):
    return await service.get_patients(request)


@router.get("/patient/{patient_id}", status_code=200)
async def get_patient(patient_id: int, request: Request):
    return await service.get_patient(patient_id, request)


@router.put("/patient/{patient_id}", status_code=200)
async def update_patient(patient_id: int, patient: PatientUpdate, request: Request):
    return await service.update_patient(patient_id, patient, request)


@router.delete("/patient/{patient_id}", status_code=204)
async def delete_patient(patient_id: int, request: Request):
    return await service.delete_patient(patient_id, request)