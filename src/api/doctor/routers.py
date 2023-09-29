from fastapi import APIRouter, Request, status

from src.api.doctor.models import DoctorEdit, DoctorOutput, DoctorRegister
from src.api.doctor.service import DoctorService

service = DoctorService()

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DoctorOutput)
async def register_doctor(body: DoctorRegister, request: Request) -> DoctorOutput:
    return await service.register_doctor(body, request)


@router.delete("/{id_doctor}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_doctor(id_doctor: int, request: Request) -> None:
    return await service.delete_doctor(id_doctor, request)


@router.put("/{id_doctor}", status_code=status.HTTP_200_OK, response_model=DoctorOutput)
async def update_doctor(
    id_doctor: int, body: DoctorEdit, request: Request
) -> DoctorOutput:
    return await service.update_doctor(id_doctor, body, request)


@router.get("/{id_doctor}", status_code=status.HTTP_200_OK, response_model=DoctorOutput)
async def get_doctor_by_id(id_doctor: int, request: Request) -> DoctorOutput:
    return await service.get_doctor_by_id(id_doctor, request)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[DoctorOutput])
async def get_all_doctor() -> list[DoctorOutput]:
    return await service.get_all_doctor()


@router.patch("/{id_doctor}/{busy_status}/{lunch_status}", status_code=status.HTTP_200_OK, response_model=DoctorOutput)
async def update_doctor_busy(id_doctor: int, request: Request, busy_status: bool = None, lunch_status: bool = None) -> DoctorOutput:
    return await service.update_doctor_busy(id_doctor, busy_status, lunch_status, request)


@router.patch("/{id_doctor}/{lunch_status}", status_code=status.HTTP_200_OK, response_model=DoctorOutput)
async def update_doctor_busy(id_doctor: int, lunch_status: bool, request: Request) -> DoctorOutput:
    return await service.update_doctor_lunch(id_doctor, lunch_status, request)