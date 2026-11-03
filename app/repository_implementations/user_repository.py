from repository_interface.user_repository import IUserRepository
from database.connection import get_connection
from models.user import User
import uuid

class UserRepository(IUserRepository):
    def create_user(self, user: User) -> None:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO user(id, acct_number, password, role) VALUES(%s, %s, %s, %s)"
            cursor.execute(sql, (user.id, user.acct_number, user.password, user.role))
            connection.commit()
            connection.close()

    def get_user_by_acct_number(self, acct_number: int) -> User | None:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user WHERE acct_number = %s"
            cursor.execute(sql, (acct_number,))
            row = cursor.fetchone()
            if row is None:
                return None
            else:
                user = User(
                    id=row[0],
                    acct_number=row[1],
                    password=row[2],
                    role=row[3]
                )
                return user

    def change_password(self, password: str, new: str) -> None:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "UPDATE user SET password = %s WHERE password = %s"
            cursor.execute(sql, (password, new))
            connection.commit()
            connection.close()

    def get_user_by_id(self, id: uuid) -> User | None:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user WHERE id = %s"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            if row is None:
                return None
            else:
                user = User(
                    id=row[0],
                    acct_number=row[1],
                    password=row[2],
                    role=row[3]
                )
                return user