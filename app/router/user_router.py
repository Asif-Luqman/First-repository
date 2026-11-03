from fastapi import APIRouter, Depends
from dependencies import get_user_service
from service_interface.i_user_service import IUserService
from dto.user_dto import CreateUserResponse

router = APIRouter(prefix= "/users", tags=["Users"])

@router.post("/users")
def create_user(service: IUserService = Depends(get_user_service)) -> CreateUserResponse:
    return service.create_user()