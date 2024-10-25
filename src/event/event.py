from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.event import Event  # Импортируйте вашу модель Event
from src.db.session import async_engine  # Импортируйте ваш engine
from src.event.schemas import EventResponse, EventCreate

router_events = APIRouter()

@router_events.post("/", response_model=EventResponse)
async def create_event(event: EventCreate):
    async with AsyncSession(async_engine) as session:
        new_event = Event(
            title=event.title,
            description=event.description,
            date=event.date,
            performers=event.performers
        )
        
        session.add(new_event)
        await session.commit()
        await session.refresh(new_event)
        
        return new_event