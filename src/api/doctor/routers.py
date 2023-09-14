from fastapi import APIRouter, Depends, Request, status

from src.api.doctor.models import DoctorRegister, DoctorOutput, DoctorEdit
from src.api.doctor.service import DoctorService

service = DoctorService()

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DoctorOutput)
async def register_doctor(body: DoctorRegister, request: Request) -> DoctorOutput:
    return await service.register_doctor(body, request)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_doctor(id_doctor: int, request: Request) -> None:
    return await service.delete_doctor(id_doctor, request)

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=DoctorOutput)
async def update_doctor(doctor_id: int, body: DoctorEdit, request: Request):
    return await service.update_doctor(doctor_id, body, request)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=DoctorOutput)
async def get_doctor_by_id(id_doctor: int, request: Request) -> DoctorOutput:
    return await service.get_doctor_by_id(id_doctor, request)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[DoctorOutput])
async def get_all_doctor() -> list[DoctorOutput]:
    return await service.get_all_doctor()
