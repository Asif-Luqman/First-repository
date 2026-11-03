from dataclasses import dataclass
import uuid

@dataclass
class User:
    id: uuid = uuid.uuid4()
    acct_number: int
    password: str
    role: str