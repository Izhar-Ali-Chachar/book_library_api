from pydantic import EmailStr
from sqlmodel import SQLModel


class BaseUser(SQLModel):
    name: str
    email: EmailStr

class UserCreate(BaseUser):
    password: str

class UserRead(BaseUser):
    id: int