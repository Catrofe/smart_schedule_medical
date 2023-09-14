from src.api.specialty.models import SpecialtyInput, SpecialtyOutput
from src.api.specialty.repository import SpecialtyRepository


class SpecialtyService:
    def __init__(self) -> None:
        self._repository = SpecialtyRepository()

    async def create_schedule(self, body: SpecialtyInput) -> SpecialtyOutput:
        specialty = await self._repository.create_schedule(body)
        return SpecialtyOutput(**specialty.dict())
