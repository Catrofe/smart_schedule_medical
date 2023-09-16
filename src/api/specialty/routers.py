from fastapi import APIRouter, Request

from src.api.specialty.models import SpecialtyInput, SpecialtyOutput
from src.api.specialty.service import SpecialtyService

service = SpecialtyService()

router = APIRouter()


@router.post("/", status_code=201, response_model=SpecialtyOutput)
async def create_schedule(body: SpecialtyInput) -> SpecialtyOutput:
    return await service.create_schedule(body)


@router.get("/", status_code=200, response_model=list[SpecialtyOutput])
async def get_all_specialty() -> list[SpecialtyOutput]:
    return await service.get_all_specialty()


@router.get("/{id_specialty}", status_code=200, response_model=SpecialtyOutput)
async def get_specialty_by_id(id_specialty: int, request: Request) -> SpecialtyOutput:
    return await service.get_specialty_by_id(id_specialty, request)


@router.delete("/{id_specialty}", status_code=204)
async def delete_specialty_by_id(id_specialty: int, request: Request) -> None:
    return await service.delete_specialty_by_id(id_specialty, request)
