from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Book
from app.schema.book import BookCreate, BookUpdate


class DatabaseServices:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id: int) -> Book | None:
        return await self.session.get(Book, id)
    
    async def add(self, create_data: BookCreate) -> Book:
        new_book = Book(
            **create_data.model_dump(),
             published_date=datetime.now()
        )

        self.session.add(new_book)
        await self.session.commit()
        await self.session.refresh(new_book)

        return new_book
    
    async def delete(self, id: int) -> None:
        book = await self.get(id)
        if book:
            await self.session.delete(book)
            await self.session.commit()

    async def update(self, id: int, update_data: BookUpdate) -> Book | None:
        book = await self.get(id)
        if not book:
            return None
        update = update_data.model_dump(exclude_none=True)
        if not update:
            return book
        book.sqlmodel_update(update)

        self.session.add(book)
        await self.session.commit()
        await self.session.refresh(book)    

        return book