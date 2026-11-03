from dataclasses import dataclass

@dataclass
class CreateAccountRequest:
    name: str
    bvn: str
    address: str

@dataclass
class CreateAccountResponse:
    acct_number: int 