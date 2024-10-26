from fastapi import HTTPException


async def add_points(
    user,
    points: float,
):
    if not user:
            raise HTTPException(status_code=404, detail="User not found.")
    
    if points < 0:
        raise HTTPException(status_code=400, detail="Cannot add a negative amount of points.")
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    user.points += points


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
