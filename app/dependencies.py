from typing import Annotated
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from .service.user import UserDatabaseService
from .database.session import get_session
from .service.book import DatabaseServices


sessionDep = Annotated[AsyncSession, Depends(get_session)]

def database_service_dep(session: sessionDep) -> DatabaseServices:
    return DatabaseServices(session)

def get_user_service_dep(
    session: sessionDep,
):
    return UserDatabaseService(session)

serviceDep = Annotated[DatabaseServices, Depends(database_service_dep)]

userServiceDep = Annotated[
    UserDatabaseService,
    Depends(get_user_service_dep),
]