import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="asifmysql@P1",
        database="account_db",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )