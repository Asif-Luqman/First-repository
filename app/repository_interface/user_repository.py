from abc import ABC, abstractmethod
from models.user import User
import uuid

class IUserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User) -> None:
        pass

    @abstractmethod
    def get_user_by_acct_number(self, acct_number: int) -> User | None:
        pass

    @abstractmethod
    def change_password(self, password: str, new: str) -> None:
        pass

    @abstractmethod
    def get_user_by_id(self, id: uuid) -> User | None:
        pass