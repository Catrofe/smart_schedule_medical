from sqlalchemy import delete, select
from sqlalchemy.sql.expression import exists

from src.api.doctor.models import DoctorEdit, DoctorRegister
from src.infra.database import Doctor, PydanticDoctor, get_session_maker


class DoctorRepository:
    def __init__(self) -> None:
        self.sessionmaker = get_session_maker()

    async def register_doctor(self, body: DoctorRegister) -> PydanticDoctor:
        async with self.sessionmaker() as session:
            save = Doctor(**body.dict())
            session.add(save)
            await session.commit()

        return PydanticDoctor.from_orm(save)

    async def verify_doctor(self, body: DoctorRegister) -> bool:
        async with self.sessionmaker() as session:
            query = await session.execute(
                select((exists(Doctor))).filter(
                    (Doctor.email == body.email)
                    | (Doctor.phoneNumber == body.phoneNumber)
                )
            )
        return bool(query.scalar())

    async def doctor_already_exist(self, id: int) -> bool:
        async with self.sessionmaker() as session:
            query = await session.execute(
                select((exists(Doctor))).filter(Doctor.id == id)
            )
        return bool(query.scalar())

    async def delete_doctor(self, id_doctor: int) -> None:
        async with self.sessionmaker() as session:
            await session.execute(delete(Doctor).where(Doctor.id == id_doctor))
            await session.commit()

    async def edit_doctor(self, id_doctor: int, body: DoctorEdit) -> PydanticDoctor:
        async with self.sessionmaker() as session:
            query = await session.execute(select(Doctor).where(Doctor.id == id_doctor))
            result = query.scalar()

            for attr, value in body.dict().items():
                if value:
                    setattr(result, attr, value)

            session.add(result)
            await session.commit()

        return PydanticDoctor.from_orm(result)

    async def get_doctor_by_id(self, id_doctor: int) -> PydanticDoctor:
        async with self.sessionmaker() as session:
            query = await session.execute(select(Doctor).where(Doctor.id == id_doctor))
        return PydanticDoctor.from_orm(query.scalar())

    async def get_all_doctor(self) -> list[PydanticDoctor]:
        async with self.sessionmaker() as session:
            query = await session.execute(select(Doctor))
            doctors = query.scalars()
        return [PydanticDoctor.from_orm(doctor) for doctor in doctors]
