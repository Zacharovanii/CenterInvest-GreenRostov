from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_users import FastAPIUsers
from src.auth.auth import auth_backend
from src.auth.schemas import UserCreate, UserRead
from src.auth.manager import get_user_manager
from src.db.models.user import User
from src.db.base_class import Base
from src.users.router import router_cache
from src.db.session import async_engine
from src.settings import settings

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def start_application():
    app = FastAPI(
        title = settings.PROJECT_NAME,
        version = settings.PROJECT_VERSION
    )
    create_tables()
    return app


app = start_application()


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app = start_application()


# Объявление роутеров
app.include_router(router_cache)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
# Объявление статичных файлов
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)
