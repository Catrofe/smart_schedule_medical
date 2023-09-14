from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.infra.database import create_database

from src.api.doctor import routers as doctor_router


app = FastAPI()

BASE_PATH = "/api/clinical"


@app.on_event("startup")
async def startup_event() -> None:
    await create_database()


@app.get("/")
async def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse(url="/docs")


app.include_router(doctor_router.router, prefix=f"{BASE_PATH}/doctors", tags=["doctors"])