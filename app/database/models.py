from datetime import datetime
from pydantic import EmailStr
from sqlmodel import SQLModel, Field

class Book(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    genre: str
    author: str
    published_date: datetime = Field(default_factory=datetime.now)

class User(SQLModel, table=True):
    __tablename__="user2"

    id: int = Field(primary_key=True)

    name: str
    email: EmailStr
    hashed_password: str