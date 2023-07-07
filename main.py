from sqlmodel import Session, select
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from db import Pressure, engine

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/pressure")
async def get_all_pressure() -> list:
    with Session(engine) as session:
        sel = select(Pressure)
        pressure = session.exec(sel).all()
    return pressure 

@app.post("/pressure/")
async def create_pressure(pressure: Pressure) -> None:
    with Session(engine) as session:
        session.add(pressure)
        session.commit()

@app.patch("/pressure/{pressure_id}")
async def update_pressure(pressure_id: int, data: Pressure) -> Pressure:
    with Session(engine) as session:
        pressure = session.get(Pressure, pressure_id)
        update_data = data.dict(exclude_unset=True)
        print(update_data)
        for key, value in update_data.items():
            setattr(pressure, key, value)
        session.add(pressure)
        session.commit()
        session.refresh(pressure)
        return pressure

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
