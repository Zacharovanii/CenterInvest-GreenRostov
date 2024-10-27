from src.points.emission_factors import Emission_factors_shopping, Emission_factors_activity, emission_factors_activity, emission_factors_shopping
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.user import User
from src.db.session import async_engine
from src.points.points import add_points
from src.users.router import current_user

router_product = APIRouter()


@router_product.post("/{user_id}/add-product")
async def add_product( 
    count_shopping: float,
    factor_shopping: Emission_factors_shopping,
    count_activity: float,
    factors_activity: Emission_factors_activity,
    user: User = Depends(current_user)
):
    async with AsyncSession(async_engine) as session:
        user = await session.get(User, user.id)
        points = (emission_factors_shopping[factor_shopping.value] * count_shopping) + (emission_factors_activity[factors_activity.value] * count_activity)

        await add_points(user, points)
        await session.commit()
