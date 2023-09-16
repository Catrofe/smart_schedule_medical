from fastapi import Request, status

from src.api.specialty.models import SpecialtyInput, SpecialtyOutput
from src.api.specialty.repository import SpecialtyRepository
from src.utils.erros_util import RaiseScheduleMedical


class SpecialtyService:
    def __init__(self) -> None:
        self._repository = SpecialtyRepository()

    async def create_schedule(self, body: SpecialtyInput) -> SpecialtyOutput:
        specialty = await self._repository.create_schedule(body)
        return SpecialtyOutput(**specialty.dict())

    async def get_all_specialty(self) -> list[SpecialtyOutput]:
        specialty = await self._repository.get_all_specialty()
        return [SpecialtyOutput(**item.dict()) for item in specialty]

    async def get_specialty_by_id(
        self, id_specialty: int, request: Request
    ) -> SpecialtyOutput:
        if not await self._repository.specialty_already_exist(id_specialty):
            raise RaiseScheduleMedical(
                request, status.HTTP_404_NOT_FOUND, "Specialty not found"
            )
        specialty = await self._repository.get_specialty_by_id(id_specialty)
        return SpecialtyOutput(**specialty.dict())

    async def delete_specialty_by_id(self, id_specialty: int, request: Request) -> None:
        if not await self._repository.specialty_already_exist(id_specialty):
            raise RaiseScheduleMedical(
                request, status.HTTP_404_NOT_FOUND, "Specialty not found"
            )
        await self._repository.delete_specialty_by_id(id_specialty)

    async def specialty_already_exist(self, id_specialty: int) -> bool:
        return await self._repository.specialty_already_exist(id_specialty)
