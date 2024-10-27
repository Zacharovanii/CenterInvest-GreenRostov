from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.achievement import Achievement
from src.db.models.user import User
from src.db.session import async_engine
from src.achievements.schemas import AchievementsRead
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy import select 
from sqlalchemy.orm.attributes import flag_modified
from src.users.router import current_user

router_achievements = APIRouter()


@router_achievements.post("/{user_id}/achievements/create-achievement")
async def create_achievement(achievement: AchievementsRead, user: User = Depends(current_user)):
    async with AsyncSession(async_engine) as session:
        user = await session.get(User, user.id)

        if user.role_id == 2:
            new_achievement = Achievement(
                title=achievement.title,
                description=achievement.description
            )
        
            session.add(new_achievement)
            await session.commit()
            await session.refresh(new_achievement)
        
            return {"message": "The achievement has been created: "}, new_achievement
        else:
            return {"message": "Insufficient permissions to create achievements."}
    

@router_achievements.get("/achievements/get-achievement/{achievement_id}")
async def get_achievement(achievement_id: int):
    async with AsyncSession(async_engine) as session:
        achievement = await session.get(Achievement, achievement_id)

        if not achievement:
            raise HTTPException(status_code=404, detail="Achievement is not found.")
        
        return {"message": f"Achievement {achievement_id}: "}, achievement
    

@router_achievements.delete("/{user_id}/achievements/get-achievement/{achievement_id}/delete-achievement")
async def delete_achievements(achievement_id: int, user: User = Depends(current_user)):
    async with AsyncSession(async_engine) as session:
        user = await session.get(User, user.id)

        if user.role_id == 2:
            achievement = await session.get(Achievement, achievement_id)

            if not achievement:
                raise HTTPException(status_code=404, detail="Achievement is not found.")

            query = select(User)
            result = await session.execute(query)
            users = result.scalars().all()

            await delete_achievement_from_users(achievement_id, users)
       
            await session.delete(achievement)
            await session.commit()

            query = select(Achievement)
            result = await session.execute(query)
            achievements = result.scalars().all()

            return {"message": "The achievement has been deleted: "}, achievements
        else:
            return {"message": "Insufficient permissions to delete achievements."}
    

async def delete_achievement_from_users(achievement_id, users):
    for user in users:
        if achievement_id in user.achievements:
            user.achievements.remove(achievement_id)
            flag_modified(user, "achievements")


@router_achievements.get("/achievements/get-achievement/{achievement_id}/get-owners")
async def get_owners(achievement_id: int):
    async with AsyncSession(async_engine) as session:
        achievement = await session.get(Achievement, achievement_id)

        if not achievement:
            raise HTTPException(status_code=404, detail="Achievement is not found.")
        
        query = select(User)
        result = await session.execute(query)
        users = result.scalars().all()

        target_users = []

        for user in users:
            if achievement_id in user.achievements:
                target_users.append(user)

        return {"message": f"Users with achievement {achievement.title}: "}, target_users
    

@router_achievements.get("/achievements/get-all-achievements")
async def get_all_achievements():
    async with AsyncSession(async_engine) as session: 
        query = select(Achievement)
        result = await session.execute(query)
        achievements = result.scalars().all()

        return {"message": "List of all achievements: "}, achievements
    

@router_achievements.put("/{user_id}/{managed_user_id}/achievements/add-achievement/{achievement_id}")
async def add_achievement_to_user(achievement_id: int, managed_user_id: int, user: User = Depends(current_user)):
    async with AsyncSession(async_engine) as session:
        user = await session.get(User, user.id)

        if user.role_id == 2:
            managed_user = await session.get(User, managed_user_id)

            if not managed_user:
                raise HTTPException(status_code=404, detail="Managed user is not found.")
        
            achievement = await session.get(Achievement, achievement_id)

            if not achievement:
                raise HTTPException(status_code=404, detail="Achievement is not found.")

            if achievement_id not in user.achievements:
                managed_user.achievements.append(achievement_id)
                achievement.owners.append(managed_user.id)
                flag_modified(achievement, "owners")
                flag_modified(managed_user, "achievements")
            else:
                return {"message": "The achievement has already been added: "}, managed_user

            await session.commit()
            await session.refresh(managed_user)

            return {"message": "The achievement has been added: "}, managed_user
        else:
            return {"message": "Insufficient permissions to add achievements."}
    

@router_achievements.delete("/{user_id}/{managed_user_id}/achievements/get-achievement/delete-achievement/{achievement_id}")
async def delete_achievement_from_user(achievement_id: int, managed_user_id: int, user: User = Depends(current_user)):
    async with AsyncSession(async_engine) as session:
        user = await session.get(User, user.id)
        
        if user.role_id == 2:
            managed_user = await session.get(User, managed_user_id)

            if not managed_user:
                raise HTTPException(status_code=404, detail="Managed user is not found.")

            achievement = await session.get(Achievement, achievement_id)

            if not achievement:
                raise HTTPException(status_code=404, detail="Achievement is not found.")

            if achievement_id in user.achievements:
                managed_user.achievements.remove(achievement_id)
                achievement.owners.remove(managed_user.id)
                flag_modified(achievement, "owners")
                flag_modified(managed_user, "achievements")
            else:
                return {"message": "Managed user does not have this achievement."}, managed_user

            await session.commit()
            await session.refresh(user)

            return {"message": "The achievement has been deleted: "}, managed_user
        else:
            return {"message": "Insufficient permissions to delete achievements."}
    

@router_achievements.get("/{user_id}/achievements/get-achievements")
async def get_events_from_user(user: User = Depends(current_user)):
    async with AsyncSession(async_engine) as session:
        user = await session.get(User, user.id)
        
        query = select(Achievement)
        result = await session.execute(query)
        achievements = result.scalars().all()

        target_achievements = []

        for achievement in achievements:
            if achievement.id in user.achievements:
                target_achievements.append(achievement)

        return {"message": "User`s achievements: "}, target_achievements
    

@router_achievements.get("/{user_id}/achievements/get-achievement/{achievement_id}")
async def get_event_from_user(achievement_id: int, user: User = Depends(current_user)):
    async with AsyncSession(async_engine) as session:
        user = await session.get(User, user.id)

        achievement = await session.get(Achievement, achievement_id)

        if not achievement:
            raise HTTPException(status_code=404, detail="Achievement is not found.")

        if achievement_id in user.achievements: 
            return True
        else:
            return False
