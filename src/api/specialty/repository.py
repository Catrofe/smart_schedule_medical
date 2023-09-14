from src.api.specialty.models import SpecialtyInput
from src.infra.database import PydanticSpecialty, Specialty, get_session_maker


class SpecialtyRepository:
    def __init__(self) -> None:
        self.sessionmaker = get_session_maker()

    async def create_schedule(self, body: SpecialtyInput) -> PydanticSpecialty:
        async with self.sessionmaker() as session:
            save = Specialty(**body.dict())
            session.add(save)
            await session.commit()

        return PydanticSpecialty.from_orm(save)
