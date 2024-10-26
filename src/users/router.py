import subprocess
import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from src.db.models.user import User
from src.db.session import async_session_maker
from src.users.schemes import UserResponse
from redis import asyncio as aioredis
from sqlalchemy.future import select
from fastapi_users import FastAPIUsers
from src.main import get_user_manager, auth_backend
from src.settings import Settings

LOCAL_REDIS_URL = "redis://127.0.0.1:6379"

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
async def start_redis():
    process = subprocess.Popen([Settings.REDIS_FILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    await asyncio.sleep(1)  
    return process

async def stop_redis(process):
    process.terminate()
    await asyncio.sleep(0.1)

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis_process = await start_redis()
    try:
        redis = aioredis.from_url(LOCAL_REDIS_URL)
        await redis.ping()  # Проверка подключения сразу
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
        yield
    finally:
        await stop_redis(redis_process)

router_cache = APIRouter(
    tags=["Страницы"],
    lifespan=lifespan
)

@router_cache.get("/profil-{id}")
@cache(expire=60)
async def profil_user(id: int):
    id = int(id)
    async with async_session_maker() as async_session:
        result = await async_session.execute(select(User).where(User.id == id))
        user_record = result.scalars().first()
        user = UserResponse(user_record) if user_record else None
    return {"user": user}
