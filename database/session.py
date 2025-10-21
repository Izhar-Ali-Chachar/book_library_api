from typing import Annotated
from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel
from fastapi import Depends

engine = create_engine(
    url="sqlite:///book.db",
    echo=True,
    connect_args={
        "check_same_thread": False
    }
)

def create_table():
    SQLModel.metadata.create_all(bind=engine)

def create_session():
    with Session(bind=engine) as session:
        yield session

sessioDb = Annotated[Session, Depends(create_session)]