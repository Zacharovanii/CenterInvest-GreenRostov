from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.event import Event
from src.db.models.user import User
from src.db.session import async_engine
from src.event.schemas import EventResponse, EventCreate
from sqlalchemy import select 

router_events = APIRouter()


@router_events.post("/create-event", response_model=EventResponse)
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


@router_events.delete("/get-event/{event_id}/delete-event")
async def delete_event(event_id: int):
    async with AsyncSession(async_engine) as session:
        event = await session.get(Event, event_id)

        query = select(User)
        result = await session.execute(query)
        users = result.scalars().all()

        # await delete_event_from_users(event, users)
        # async for user in users:
            
        #     if event.id in user.events:
        #         user.events.remove(event.id)

        #     yield session.commit()
            

        # await session.delete(event)
        # await session.commit()

        # query = select(Event)
        # result = await session.execute(query)
        # events = result.scalars().all()

        return {"message": "event deleted."}#, events
    

# async def delete_event_from_users(event, users):
#     for user in users:
#         if event.id in user.events:
#             user.events.remove(event.id)


@router_events.get("/get-all-events")
async def get_all_events():
    async with AsyncSession(async_engine) as session: 
        query = select(Event)
        result = await session.execute(query)
        events = result.scalars().all()

        return events
    

@router_events.get("/get-event/{event_id}")
async def get_event(event_id: int):
    async with AsyncSession(async_engine) as session:
        event = await session.get(Event, event_id)

        return event
