from src.points.emission_factors import Emission_factors, emission_factors
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.user import User
from src.db.session import async_engine
from src.points.points import add_points

router_product = APIRouter()


@router_product.post("/{user_id}/add-product")
async def add_product(
    user_id: int, 
    count: float,
    factor: Emission_factors
):
    async with AsyncSession(async_engine) as session:

        user = await session.get(User, user_id)
        
        points = emission_factors[factor.value] * count

        await add_points(user, points)
        await session.commit()
