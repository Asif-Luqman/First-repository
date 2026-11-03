from app.dto.account_dto import CreateAccountRequest, CreateAccountResponse
from service_interface.i_account_service import IAccountService
from models.account import Account
from repository_interface.account_repository import IAccountRepository

class AccountService(IAccountService):
    def __init__(self, account_repository: IAccountRepository):
        self.account_repository = account_repository

    def create_account(self, request: CreateAccountRequest) -> CreateAccountResponse:
        account = Account(name=request.name, bvn=request.bvn, address=request.address)
        self.account_repository.create_account(account)
        response = CreateAccountResponse(acct_number=account.acct_number)
        return response
    
