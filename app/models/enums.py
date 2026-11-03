from enum import Enum

class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

class AccountType(str, Enum):
    CURRENT = "Current"
    SAVINGS = "Savings"