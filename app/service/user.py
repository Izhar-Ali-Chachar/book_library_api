from datetime import timedelta
import jwt
from pydantic import EmailStr
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import AsyncSession

from passlib.context import CryptContext # type: ignore #noqa
from sqlmodel import select

from ..utils import encode_token 

pass_ctx = CryptContext(schemes=["argon2"], deprecated="auto")

from ..schema.user import UserCreate

from ..database.models import User


class UserDatabaseService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register_user(self, credentials: UserCreate) -> User:
        new_user = User(
            **credentials.model_dump(exclude={"password"}),
            hashed_password=pass_ctx.hash(credentials.password),
        )

        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return new_user
    
    async def login_user(self, email: EmailStr, password: str) -> dict:
        query: Result = await self.session.execute(
            select(User).where(User.email == email)
        )
        user = query.scalar()

        if not user or not pass_ctx.verify(password, user.hashed_password):
            raise Exception("Invalid credentials")
        
        payload = {
                "id": user.id,
                "email": user.email,
            }
        
        token = encode_token(payload, exp=timedelta(days=3))

        return {
            "access_token": token,
            "token_type": "bearer",
        }