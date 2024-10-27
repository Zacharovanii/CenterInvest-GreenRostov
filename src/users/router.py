import subprocess
import asyncio
import os
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter, Depends, UploadFile, File
from fastapi_cache import FastAPICache
from fastapi.responses import FileResponse
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from src.db.models.user import User
from src.db.session import async_session_maker
from src.auth.schemas import UserResponse
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
    lifespan=lifespan
)

@router_cache.get("/profile-{id}")
@cache(expire=60)
async def profile_user(id: int):
    id = int(id)
    async with async_session_maker() as async_session:
        result = await async_session.execute(select(User).where(User.id == id))
        user_record = result.scalars().first()
        user = UserResponse(user_record) if user_record else None
    return {"user": user}

@router_cache.get("/my-profile")
@cache(expire=120)
async def my_profile(user: User = Depends(current_user)):
    async with async_session_maker() as async_session:
        result = await async_session.execute(select(User).where(User.id == user.id))
        user_record = result.scalars().first()
        user = UserResponse(user_record) if user_record else None
    return {"state": 200, "user": user}




AVATAR_DIR = "avatars"

async def upload_avatar(user_id: int, file: UploadFile = File(...)):
    if not os.path.exists(AVATAR_DIR):
        os.makedirs(AVATAR_DIR)

    file_path = os.path.join(AVATAR_DIR, f"{user_id}.jpeg")
    
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    return {"filename": file.filename}

from fastapi import Depends

async def get_avatar(user_id: int):
    file_path = os.path.join(AVATAR_DIR, f"{user_id}.jpeg")
    default_avatar_path = os.path.join(AVATAR_DIR, "1.jpeg")

    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return FileResponse(default_avatar_path)

async def remove_avatar(user_id: int):
    file_path = os.path.join(AVATAR_DIR, f"{user_id}.jpeg")
    default_avatar_path = os.path.join(AVATAR_DIR, "1.jpeg")
    
    if os.path.exists(file_path):
        os.remove(file_path)
        return {"state": 200, "description": "Your avatar has been reset to standard."}
    else:
        return {"state": 200, "description": "Your avatar is standard."}

from fastapi import FastAPI, Depends

@router_cache.post("/users/{user_id}/avatar")
async def upload_avatar_endpoint(user: User = Depends(current_user), file: UploadFile = File(...)):
    user_id = user.id
    return await upload_avatar(user_id, file)

@router_cache.get("/users/{user_id}/avatar")
async def get_avatar_endpoint(user_id: int):
    return await get_avatar(user_id)


@router_cache.delete("/users/{user_id}/avatar")
async def remove_avatar_endpoint(user: User = Depends(current_user)):
    user_id = user.id
    return await remove_avatar(user_id)