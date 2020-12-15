import sqlite3


class SqlManager:
    def __init__(self, db_filename: str):
        self.db_filename = db_filename
        self.con = sqlite3.connect(db_filename)
        self.cur = self.con.cursor()

    def get_user(self, username: str) -> list:
        res = self.cur.execute(
            'SELECT * FROM user WHERE username = ?',
            (username,)
        )
        return res.fetchall()

    def add_user(self, username: str, pwd_hash: str, email: str):
        self.cur.execute(
            'INSERT INTO user (username, password_hash, email)'
            'VALUES (?, ?, ?)', (username, pwd_hash, email)
        )
        self.con.commit()
