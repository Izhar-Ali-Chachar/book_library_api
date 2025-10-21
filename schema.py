from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class BaseBook(BaseModel):
    name: str
    genre: str
    author: str

class BookRead(BaseBook):
    id: int
    publication_date: date | None = None

class BookCreate(BaseBook):
    pass

class BookUpdate(BaseModel):
    name: str | None = Field(default=None)
    publication_date: date | None = Field(default=None)
    genre: str | None = Field(default=None)
    author: str | None = Field(default=None)

