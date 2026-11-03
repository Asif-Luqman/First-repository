from dataclasses import dataclass
import uuid
import random

@dataclass
class Account:
    id: uuid = uuid.uuid4
    name: str
    acct_number: int = random.randint(1000000000, 9999999999)
    bvn: int
    address: str
    balance: float