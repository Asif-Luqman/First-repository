from repository_implementations.user_repository import UserRepository
from repository_implementations.account_repository import AccountRepository
from service_implementations.user_service import UserService
from service_implementations.account_service import AccountService

def get_user_service():
    repository = UserRepository()
    service = UserService(repository)
    return service

def get_account_service():
    repository = AccountRepository()
    service = AccountService(repository)
    return service