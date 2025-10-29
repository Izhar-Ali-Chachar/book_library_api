from typing import Annotated
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from .database.session import get_session
from .service.book import DatabaseServices


sessionDep = Annotated[AsyncSession, Depends(get_session)]

def database_service_dep(session: sessionDep) -> DatabaseServices:
    return DatabaseServices(session)

serviceDep = Annotated[DatabaseServices, Depends(database_service_dep)]