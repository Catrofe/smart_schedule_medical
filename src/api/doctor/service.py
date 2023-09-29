from typing import Optional, Union

from fastapi import Request, status

from src.api.doctor.models import DoctorEdit, DoctorOutput, DoctorRegister
from src.api.doctor.repository import DoctorRepository
from src.api.specialty.service import SpecialtyService
from src.utils.erros_util import RaiseScheduleMedical
from src.utils.settings import Settings
import requests


class DoctorService:
    def __init__(self) -> None:
        self._repository = DoctorRepository()

    async def register_doctor(
        self, body: DoctorRegister, request: Request
    ) -> DoctorOutput:
        await self.validation_doctor(request, body=body, id_specialty=body.specialtyId)
        doctor = await self._repository.register_doctor(body)
        return DoctorOutput(**doctor.dict())

    async def delete_doctor(self, id_doctor: int, request: Request) -> None:
        await self.validation_doctor(request, id_doctor=id_doctor)
        await self._repository.delete_doctor(id_doctor)

    async def update_doctor(
        self, id_doctor: int, body: DoctorEdit, request: Request
    ) -> DoctorOutput:
        await self.validation_doctor(
            request, body=body, id_doctor=id_doctor, id_specialty=body.specialtyId
        )
        doctor = await self._repository.edit_doctor(id_doctor, body)
        return await self.get_doctor_by_id(doctor.id, request)

    async def get_doctor_by_id(self, id_doctor: int, request: Request) -> DoctorOutput:
        await self.validation_doctor(request, id_doctor=id_doctor)
        doctor = await self._repository.get_doctor_by_id(id_doctor)
        return DoctorOutput(**doctor.dict())

    async def get_all_doctor(self) -> list[DoctorOutput]:
        doctors = await self._repository.get_all_doctor()
        return [DoctorOutput(**doctor.dict()) for doctor in doctors]

    async def validation_doctor(
        self,
        request: Request,
        id_doctor: Optional[int] = None,
        id_specialty: Optional[int] = None,
        body: Optional[Union[DoctorRegister, DoctorEdit]] = None,
    ) -> None:
        if id_specialty and not await SpecialtyService().specialty_already_exist(
            id_specialty
        ):
            raise RaiseScheduleMedical(
                request, status.HTTP_400_BAD_REQUEST, "Specialty not found"
            )
        if id_doctor and not await self._repository.doctor_already_exist(id_doctor):
            raise RaiseScheduleMedical(
                request, status.HTTP_409_CONFLICT, "Doctor already exists"
            )
        if body and await self._repository.verify_doctor(body):
            raise RaiseScheduleMedical(
                request, status.HTTP_409_CONFLICT, "Doctor already exists"
            )

    async def update_doctor_busy_and_lunch(self, id_doctor: int, busy_status: Optional[bool], lunch_status: Optional[bool], request: Request) -> DoctorOutput:
        await self.validation_doctor(request, id_doctor=id_doctor)

        if busy_status is not None:
            await self._repository.update_doctor_busy(id_doctor, busy_status)
        if lunch_status is not None:
            await self._repository.update_doctor_lunch(id_doctor, lunch_status)

        doctor = await self._repository.get_doctor_by_id(id_doctor)

        if not doctor.busy and not doctor.lunch:
            return DoctorOutput(**doctor.dict())
