from src.infra.database import get_session_maker


class ScheduleRepository:
    def __init__(self) -> None:
        self.sessionmaker = get_session_maker()
