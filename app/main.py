from fastapi import FastAPI
from contextlib import asynccontextmanager

from .database.session import create_table
from .routers.router import master_router

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    await create_table()
    yield

app = FastAPI(lifespan=lifespan_handler)

app.include_router(router=master_router)
