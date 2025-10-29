from pydantic import EmailStr
from sqlmodel import SQLModel


class BaseUser(SQLModel):
    username: str
    email: EmailStr

class UserCreate(BaseUser):
    password: str

class UserRead(BaseUser):
    id: int