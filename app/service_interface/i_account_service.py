from abc import ABC, abstractmethod
from dto.account_dto import CreateAccountRequest

class IAccountService(ABC):
    @abstractmethod
    def create_account(self, request: CreateAccountRequest) -> None:
        pass