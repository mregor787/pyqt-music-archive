import sqlite3

from typing import List


class SqlManager:
    def __init__(self, db_filename: str):
        self.db_filename = db_filename
        self.con = sqlite3.connect(db_filename)
        self.cur = self.con.cursor()

    def get_user(self, username: str) -> List[dict]:
        res = self.cur.execute(
            'SELECT * FROM user WHERE username = ?',
            (username,)
        )
        col_names = [col[0] for col in res.description]
        return [dict(zip(col_names, row)) for row in res]

    def add_user(self, username: str, pwd_hash: str, email: str, icon_path: str):
        self.cur.execute(
            'INSERT INTO user (username, password_hash, email)'
            'VALUES (?, ?, ?, ?)', (username, pwd_hash, email, icon_path)
        )
        self.con.commit()
