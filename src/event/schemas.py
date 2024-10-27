from datetime import datetime
from pydantic import BaseModel


class EventModel(BaseModel):
    title: str
    description: str
    date: datetime
    organizer: int

    class Config:
        orm_mode = True