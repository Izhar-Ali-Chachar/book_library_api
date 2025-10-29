from typing import Any

from fastapi import FastAPI, status
from contextlib import asynccontextmanager

from .database.session import create_table
from .database.models import Book
from .schema.book import  BookCreate, BookRead, BookUpdate
from .dependencies import serviceDep

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    await create_table()
    yield

app = FastAPI(lifespan=lifespan_handler)

@app.get('/book')
async def get_books(id: int, service: serviceDep):
    return await service.get(id)

@app.post("/book")
async def create_book(book_data: BookCreate, service: serviceDep) -> Book:
    new_book = await service.add(book_data)
    return new_book

@app.patch("/book", response_model=BookRead)
async def update_book(id: int, update_data: BookUpdate, service: serviceDep):
    return await service.update(id, update_data)

@app.delete("/book", status_code=status.HTTP_200_OK)
async def delete_book(id: int, service: serviceDep):
    await service.delete(id)
    return {"detail": f"Shipment with id #{id} is deleted!"}