from datetime import datetime
from typing import List
from pydantic import BaseModel

class EventCreate(BaseModel):
    title: str
    description: str
    date: datetime
    performers: List[int]

class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    date: datetime
    performers: List[int]

    class Config:
        orm_mode = True  # Позволяет использовать ORM-объекты