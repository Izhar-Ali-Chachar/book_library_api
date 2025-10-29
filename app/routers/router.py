from fastapi import APIRouter

from ..routers import book, user

master_router = APIRouter()

master_router.include_router(book.router)
master_router.include_router(user.router)
