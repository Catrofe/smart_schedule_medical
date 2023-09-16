from fastapi import Request, status

from src.api.doctor.models import DoctorEdit, DoctorOutput, DoctorRegister
from src.api.doctor.repository import DoctorRepository
from src.utils.erros_util import RaiseScheduleMedical


class DoctorService:
    def __init__(self) -> None:
        self._repository = DoctorRepository()

    async def register_doctor(
        self, body: DoctorRegister, request: Request
    ) -> DoctorOutput:
        doctor_exist = await self._repository.verify_doctor(body)
        if not doctor_exist:
            doctor = await self._repository.register_doctor(body)
            return DoctorOutput(**doctor.dict())
        raise RaiseScheduleMedical(
            request, status.HTTP_409_CONFLICT, "Doctor already exists"
        )

    async def delete_doctor(self, id_doctor: int, request: Request) -> None:
        doctor_exist = await self._repository.doctor_already_exist(id_doctor)
        if not doctor_exist:
            raise RaiseScheduleMedical(
                request, status.HTTP_400_BAD_REQUEST, "Doctor not exists"
            )
        await self._repository.delete_doctor(id_doctor)

    async def update_doctor(
        self, id_doctor: int, body: DoctorEdit, request: Request
    ) -> DoctorOutput:
        doctor_exist = await self._repository.doctor_already_exist(id_doctor)
        if not doctor_exist:
            raise RaiseScheduleMedical(
                request, status.HTTP_400_BAD_REQUEST, "Doctor not exists"
            )
        doctor = await self._repository.edit_doctor(id_doctor, body)
        return await self.get_doctor_by_id(doctor.id, request)

    async def get_doctor_by_id(self, id_doctor: int, request: Request) -> DoctorOutput:
        doctor_exist = await self._repository.doctor_already_exist(id_doctor)
        if not doctor_exist:
            raise RaiseScheduleMedical(
                request, status.HTTP_400_BAD_REQUEST, "Doctor not exists"
            )
        doctor = await self._repository.get_doctor_by_id(id_doctor)
        return DoctorOutput(**doctor.dict())

    async def get_all_doctor(self) -> list[DoctorOutput]:
        doctors = await self._repository.get_all_doctor()
        return [DoctorOutput(**doctor.dict()) for doctor in doctors]
