from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.user import User
from src.db.session import async_engine
from src.roles.schemas import Roles
from sqlalchemy import select 
from src.users.router import current_user

router_roles = APIRouter()


@router_roles.get("/roles/get-{title}")
async def get_organizes(title: Roles):
    async with AsyncSession(async_engine) as session:
        query = select(User)
        result = await session.execute(query)
        users = result.scalars().all()

        target_users = []

        for user in users:
            if (user.role_id == 0 and title.value == 'user') or (user.role_id == 1 and title.value == 'organizer') or (user.role_id == 2 and title.value == 'admin'):
                target_users.append(user)

        return {"message": f"Users with role {title.value}: "}, target_users
    

@router_roles.put("/{user_id}/{managed_user_id}/{new_role}")
async def assign_role(managed_user_id: int, new_role: Roles, user: User = Depends(current_user)):
    async with AsyncSession(async_engine) as session:
        user = await session.get(User, user.id)

        if user.role_id == 2:
            managed_user = await session.get(User, managed_user_id)

            if not managed_user:
                raise HTTPException(status_code=404, detail="Managed user is not found.")
            
            match (new_role.value):
                case 'user':
                    new_role_id = 0
                case 'organizer':
                    new_role_id = 1
                case 'admin':
                    new_role_id = 2

            managed_user.role_id = new_role_id

            await session.commit()
            await session.refresh(managed_user)

            return {"message": "The role has been assigned: "}, managed_user
        else:
            return {"message": "Insufficient permissions to assign roles."}
