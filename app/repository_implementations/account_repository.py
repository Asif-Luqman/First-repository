from repository_interface.account_repository import IAccountRepository
from models.account import Account
from database.connection import get_connection

class AccountRepository(IAccountRepository):
    def create_account(self, account: Account) -> None:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO account(id, name, acct_number, bvn, address, balance) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (account.id, account.name, account.acct_number, account.bvn, account.address, account.balance))
            connection.commit()
            connection.close()

    def get_account_by_acct_num(self, acct_number: int) -> Account | None:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM account WHERE acct_number = %s"
            cursor.execute(sql, (acct_number,))
            row = cursor.fetchone()
            if row is None:
                return None
            else:
                account = Account(
                    id=row[0],
                    name=row[1],
                    acct_number=row[2],
                    bvn=row[3],
                    address=row[4],
                    balance=row[5]
                )
                return account

