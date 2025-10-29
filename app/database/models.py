from datetime import datetime
from sqlmodel import SQLModel, Field

class Book(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    genre: str
    author: str
    published_date: datetime = Field(default_factory=datetime.now)