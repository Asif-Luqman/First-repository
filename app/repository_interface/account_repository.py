from abc import ABC, abstractmethod
from models.account import Account

class IAccountRepository(ABC):
    @abstractmethod
    def create_account(self, account: Account) -> None:
        pass

    @abstractmethod
    def get_account_by_acct_num(self, acct_number: int) -> Account | None:
        pass

    # @abstractmethod
    # def deposit