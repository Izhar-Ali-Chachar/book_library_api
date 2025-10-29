from fastapi import APIRouter

from ..schema.user import UserCreate, UserRead

from ..dependencies import userServiceDep

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserRead)
async def register_user(user_data: UserCreate, service: userServiceDep):
    new_user = await service.register_user(user_data)
    return new_user
    