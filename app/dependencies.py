from typing import Annotated
from fastapi import Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from .database.models import User

from .service.user import UserDatabaseService
from .database.session import get_session
from .service.book import BookDatabaseService
from .utils import decode_token
from .core.security import oauth_scheme

sessionDep = Annotated[AsyncSession, Depends(get_session)]

def database_service_dep(session: sessionDep) -> BookDatabaseService:
    return BookDatabaseService(session)

def get_user_service_dep(
    session: sessionDep,
):
    return UserDatabaseService(session)

def get_access_token(token: Annotated[str, Depends(oauth_scheme)]) -> dict | None:
    data = decode_token(token)

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid token",
        )

    return data

async def get_current_seller(
        session: sessionDep,
        token_data: dict = Depends(get_access_token),
):
    return await session.get(User, token_data["id"])

userDep = Annotated[User, Depends(get_current_seller)]

bookServiceDep = Annotated[BookDatabaseService, Depends(database_service_dep)]

userServiceDep = Annotated[
    UserDatabaseService,
    Depends(get_user_service_dep),
]