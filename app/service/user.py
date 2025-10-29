from sqlalchemy.ext.asyncio import AsyncSession

from passlib.context import CryptContext # type: ignore #noqa

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