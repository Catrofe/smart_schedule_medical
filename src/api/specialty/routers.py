from fastapi import APIRouter

from src.api.specialty.models import SpecialtyInput, SpecialtyOutput
from src.api.specialty.service import SpecialtyService

service = SpecialtyService()

router = APIRouter()


@router.post("/", status_code=201, response_model=SpecialtyOutput)
async def create_schedule(body: SpecialtyInput) -> SpecialtyOutput:
    return await service.create_schedule(body)
