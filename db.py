from typing import Optional
from datetime import datetime

from sqlmodel import Field, SQLModel, create_engine

class Pressure(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    top: int
    bot: int
    pulse: int
    time: datetime = Field(default=datetime.now())

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)
