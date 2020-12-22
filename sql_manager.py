import sqlite3


class SqlManager:
    def __init__(self, db_filename: str):
        self.db_filename = db_filename
        self.con = sqlite3.connect(db_filename)
        self.cur = self.con.cursor()

    def get_user(self, username: str) -> dict:
        res = self.cur.execute(
            'SELECT * FROM user WHERE username = ?',
            (username,)
        )
        col_names = [col[0] for col in res.description]
        return [dict(zip(col_names, row)) for row in res][0]

    def add_user(self, user_data: dict):
        query = 'INSERT INTO user (' + ', '.join(user_data.keys()) + ') VALUES (' + \
                ', '.join(['?'] * len(user_data.keys())) + ')'
        self.cur.execute(
            query, (*(user_data.values()),)
        )
        self.con.commit()
