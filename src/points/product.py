from src.points.emission_factors import Emission_factors_shopping, Emission_factors_activity, emission_factor_shopping, emission_factor_activity
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.user import User
from src.db.session import async_engine
from src.points.points import add_points

router_product = APIRouter()


@router_product.post("/{user_id}/add-product")
async def add_product(
    user_id: int, 
    count_shopping: float,
    count_activity: float,
    factor_shopping: Emission_factors_shopping,
    factor_activity: Emission_factors_activity
):
    async with AsyncSession(async_engine) as session:

        user = await session.get(User, user_id)
        
        points = (emission_factor_shopping[factor_shopping.value] * count_shopping) + (emission_factor_activity[factor_activity.value] * count_activity)

        await add_points(user, points)
        await session.commit()
