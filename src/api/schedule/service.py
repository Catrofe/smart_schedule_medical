from src.api.schedule.repository import ScheduleRepository


class ScheduleService:
    def __init__(self) -> None:
        self._repository = ScheduleRepository()
