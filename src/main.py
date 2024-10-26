from enum import Enum
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from src.auth.auth import auth_backend
from src.auth.schemas import UserCreate, UserRead
from src.auth.manager import get_user_manager
from src.db.models.user import User
from src.settings import settings
from fastapi.middleware.cors import CORSMiddleware
from src.event.event import router_events
from src.points.product import router_product
from src.users.router import router_cache


app = FastAPI(
        title = settings.PROJECT_NAME,
        version = settings.PROJECT_VERSION
    )


origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Tags(Enum):
    users = 'users_funcs'
    events = 'events_funcs'
    points = 'points_funcs'
    cache = 'cache'
    pages = 'pages'


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


# Объявление роутеров
app.include_router(
    router_cache,
    tags=[Tags.users],
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=[Tags.users],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=[Tags.users],
)
app.include_router(
    router_events,
    prefix="/events",
    tags=[Tags.events]
)
app.include_router(
    router_product,
    prefix="/users",
    tags=[Tags.points]
)