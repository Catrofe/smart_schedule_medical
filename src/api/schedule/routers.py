from fastapi import APIRouter

from src.api.schedule.service import ScheduleService

service = ScheduleService()

router = APIRouter()
