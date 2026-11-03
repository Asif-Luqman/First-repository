from repository_interface.user_repository import IUserRepository
from service_interface.i_user_service import IUserService
from models.user import User
from dto.user_dto import LoginRequest, LoginResponse, ChangePasswordRequest, ResetPasswordRequest, CreateUserRequest, CreateUserResponse

class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def create_user(self, request: CreateUserRequest) -> None:
        user = User(acct_number=request.acct_number, password=request.password, role= request.role)
        self.user_repository.create_user(user)
        response = CreateUserResponse(user.acct_number)
        return response

    def login(self, request: LoginRequest) -> None:
        user = self.user_repository.get_user_by_acct_number(request.acct_number)
        if user is not None:
            if request.password == user.password:
                response = LoginResponse(user.acct_number)
                return response            
        else:
            return None

    def change_password(self, request: ChangePasswordRequest) -> None:
        user = self.user_repository.get_user_by_id(request.id)
        if user is not None:
            if request.new_password == request.confirm_new:
                self.user_repository.change_password(request.password, request.new_password)
        else:
            return None
                
    def reset_password(self, request: ResetPasswordRequest) -> None:
        user = self.user_repository.get_user_by_id(request.id)
        if user is not None:
            self.user_repository.change_password(request.password, new= None)
        else:
            return None