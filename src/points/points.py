from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter
from src.db.session import async_engine

router = APIRouter()
@router.put("/level-update")
async def level_update(user):
    async with AsyncSession(async_engine) as session:
        if user.points < 100:
            user.level = 1
        elif user.points < 200:
            user.level = 2
        elif user.points < 300:
            user.level = 3
        elif user.points < 400:
            user.level = 4
        elif user.points < 500:
            user.level = 5
        elif user.points < 600:
            user.level = 6
        elif user.points < 700:
            user.level = 7
        elif user.points < 800:
            user.level = 8
        elif user.points < 900:
            user.level = 9
        elif user.points < 1000:
            user.level = 10
        
        await session.commit()

        return{"message": f"level {user.id} was up to {user.level}"}


async def add_points(
    user,
    points: float,
):
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    if points < 0:
        raise HTTPException(status_code=400, detail="Cannot add a negative amount of points.")
    
    
    user.points += points

    await level_update(user)


async def remove_points(
    user,
    points: int,
):
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
        
    if points < 0:
        raise HTTPException(status_code=400, detail="Cannot remove a negative amount of points.")
    
    if user.points < points:
        user.points = 0
    else:
        user.points -= points

    await level_update(user)
