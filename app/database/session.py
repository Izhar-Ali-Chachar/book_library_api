from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlmodel import Session, SQLModel
from fastapi import Depends

engine = create_async_engine(
    url="sqlite:///book.db",
    echo=True,
)

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def create_session():
    async with AsyncSession(engine) as session:
        yield session