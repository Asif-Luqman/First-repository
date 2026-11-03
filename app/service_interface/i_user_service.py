from abc import ABC, abstractmethod
from dto.user_dto import LoginRequest, ChangePasswordRequest, ResetPasswordRequest, CreateUserRequest

class IUserService(ABC):
    @abstractmethod
    def create_user(self, reguest: CreateUserRequest) -> None:
        pass
    
    @abstractmethod
    def login(self, request: LoginRequest) -> None:
        pass

    @abstractmethod
    def change_password(self, request: ChangePasswordRequest) -> None:
        pass

    @abstractmethod
    def reset_password(self, request: ResetPasswordRequest) -> None:
        pass