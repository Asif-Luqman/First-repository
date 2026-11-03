from dataclasses import dataclass
import uuid

@dataclass
class CreateUserRequest:
    acct_number: int
    password: str
    role: str

@dataclass
class CreateUserResponse:
    id: uuid
    acct_number: int

@dataclass
class LoginRequest:
    acct_number: int
    password: str

@dataclass
class LoginResponse:
    id: uuid
    acct_number: int

@dataclass
class ChangePasswordRequest:
    id: uuid
    new_password: str
    confirm_new: str

@dataclass
class ResetPasswordRequest:
    id: uuid
    password: str