from typing import Annotated
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import create_session
from app.service.book import DatabaseServices


sessionDep = Annotated[AsyncSession, Depends(create_session)]

def database_service_dep(session: sessionDep) -> DatabaseServices:
    return DatabaseServices(session)

serviceDep = Annotated[DatabaseServices, Depends(database_service_dep)]