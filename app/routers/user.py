from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..schema.user import UserCreate, UserRead

from ..dependencies import userServiceDep

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserRead)
async def register_user(user_data: UserCreate, service: userServiceDep):
    new_user = await service.register_user(user_data)
    return new_user

@router.post("/login")
async def login_user(
    request_form: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: userServiceDep,
):
    token = await service.login_user(
        email=request_form.username,
        password=request_form.password,
    )
    return {"access_token": token, "token_type": "bearer"}
