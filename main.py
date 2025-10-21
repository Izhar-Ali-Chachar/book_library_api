from typing import Any
from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from .database.session import create_table, sessioDb
from .database.models import Book
from .schema import  BookCreate, BookRead, BookUpdate

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    create_table()
    yield

app = FastAPI(lifespan=lifespan_handler)

@app.get('/book', response_model=BookRead)
def get_books(id: int, session: sessioDb):
    book = session.get(Book, id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="id not found"
        )
    return book

@app.post("/book", response_model=None)
def create_book(book_data: BookCreate, session: sessioDb) -> dict[str, int]:
    new_book = Book(
        **book_data.model_dump()
    )

    session.add(new_book)
    session.commit()
    session.refresh(new_book)

    return {"id": new_book.id}

@app.patch("/book", response_model=BookRead)
def update_book(id: int, update_data: BookUpdate, session: sessioDb):
    update = update_data.model_dump(exclude_none=True)

    if not update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data provided to update",
        )

    book = session.get(Book, id)
    if book is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    book.sqlmodel_update(update)

    session.add(book)
    session.commit()
    session.refresh(book)

    return book

@app.delete("/book", status_code=status.HTTP_200_OK)
def delete_book(id: int, session: sessioDb):
    session.delete(
        session.get(Book, id)
    )

    session.commit()

    return {"detail": f"Shipment with id #{id} is deleted!"}