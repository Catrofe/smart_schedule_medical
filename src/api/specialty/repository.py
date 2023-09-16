from sqlalchemy import delete, select

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

    async def get_all_specialty(self) -> list[PydanticSpecialty]:
        async with self.sessionmaker() as session:
            query = await session.execute(select(Specialty))
            specialtys = query.scalars()

        return [PydanticSpecialty.from_orm(specialty) for specialty in specialtys]

    async def specialty_already_exist(self, id_specialty: int) -> bool:
        async with self.sessionmaker() as session:
            query = await session.execute(
                select(Specialty).where(Specialty.id == id_specialty)
            )

        return bool(query.scalar())

    async def get_specialty_by_id(self, id_specialty: int) -> PydanticSpecialty:
        async with self.sessionmaker() as session:
            query = await session.execute(
                select(Specialty).filter(Specialty.id == id_specialty)
            )
            specialty = query.scalar()

        return PydanticSpecialty.from_orm(specialty)

    async def delete_specialty_by_id(self, id_specialty: int) -> None:
        async with self.sessionmaker() as session:
            await session.execute(
                delete(Specialty).filter(Specialty.id == id_specialty)
            )
            await session.commit()
