from sqlalchemy import delete, select

from src.infra.database import PydanticPatient, get_session_maker


class PatientRepository:
    def __init__(self) -> None:
        self.sessionmaker = get_session_maker()

    async def create_patient(self, patient: PydanticPatient) -> PydanticPatient:
        async with self.sessionmaker() as session:
            async with session.begin():
                session.add(patient)
                await session.commit()
                await session.refresh(patient)
                return patient

    async def get_patients(self) -> List[PydanticPatient]:
        async with self.sessionmaker() as session:
            async with session.begin():
                query = select(PydanticPatient)
                result = await session.execute(query)
                return result.scalars().all()

    async def get_patient(self, patient_id: int) -> PydanticPatient:
        async with self.sessionmaker() as session:
            async with session.begin():
                query = select(PydanticPatient).where(PydanticPatient.id == patient_id)
                result = await session.execute(query)
                return result.scalars().first()

    async def update_patient(self, patient_id: int, patient: PydanticPatient) -> PydanticPatient:
        async with self.sessionmaker() as session:
            async with session.begin():
                query = (
                    update(PydanticPatient)
                    .where(PydanticPatient.id == patient_id)
                    .values(**patient.dict())
                )
                await session.execute(query)
                await session.commit()
                return patient

    async def delete_patient(self, patient_id: int) -> None:
        async with self.sessionmaker() as session:
            async with session.begin():
                query = delete(PydanticPatient).where(PydanticPatient.id == patient_id)
                await session.execute(query)
                await session.commit()
                return None