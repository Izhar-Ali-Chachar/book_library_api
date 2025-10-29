from fastapi import APIRouter, status

from ..database.models import Book

from ..dependencies import serviceDep
from ..schema.book import BookCreate, BookRead, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])

@router.get('/{id}')
async def get_books(id: int, service: serviceDep):
    return await service.get(id)

@router.post("/")
async def create_book(book_data: BookCreate, service: serviceDep) -> Book:
    new_book = await service.add(book_data)
    return new_book

@router.patch("/{id}", response_model=BookRead)
async def update_book(id: int, update_data: BookUpdate, service: serviceDep):
    return await service.update(id, update_data)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_book(id: int, service: serviceDep):
    await service.delete(id)
    return {"detail": f"Book with id #{id} is deleted!"}