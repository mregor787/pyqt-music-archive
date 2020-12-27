import sqlite3

from typing import List


class SqlManager:
    def __init__(self, db_filename: str):
        self.db_filename = db_filename
        self.con = sqlite3.connect(db_filename)
        self.cur = self.con.cursor()

    @staticmethod
    def get_dicts(res) -> List[dict]:
        col_names = [col[0] for col in res.description]
        data = [dict(zip(col_names, row)) for row in res]
        return data if data else []

    def get_user(self, username: str):
        res = self.cur.execute(
            'SELECT * FROM user WHERE username = ?',
            (username,)
        )
        data = self.get_dicts(res)
        return data[0] if data else []

    def add_user(self, user_data: dict):
        query = 'INSERT INTO user (' + ', '.join(user_data.keys()) + ') VALUES (' + \
                ', '.join(['?'] * len(user_data.keys())) + ')'
        self.cur.execute(
            query, (*(user_data.values()),)
        )
        self.con.commit()

    def update_user(self, username: str, update_data: dict):
        query = 'UPDATE user SET (' + ', '.join(update_data.keys()) + ') = (' + \
                ', '.join(['?'] * len(update_data.keys())) + ') WHERE username = ?'
        self.cur.execute(
            query, (*(update_data.values()), username)
        )
        self.con.commit()

    def get_all_table_items(self, table: str) -> List[dict]:
        res = self.cur.execute(f'SELECT * FROM {table}')
        return self.get_dicts(res)

    def get_table_items_by_partial_title(self, table: str, partial_title: str) -> List[dict]:
        parameter = 'name' if table in ['artist', 'genre'] else 'title'
        res = self.cur.execute(
            f'SELECT * FROM {table} WHERE {parameter} LIKE ?', (f'%{partial_title}%',)
        )
        return self.get_dicts(res)

    def get_table_items_by_parameter(self, table: str, parameter: str, value: int, sign: str) -> List[dict]:
        query = f'SELECT * FROM {table} WHERE {parameter} {sign} ?'
        res = self.cur.execute(query, (value,))
        return self.get_dicts(res)

    def get_artist_by_album(self, album: str) -> List[dict]:
        res = self.cur.execute(
            f'''SELECT * FROM artist WHERE id = (SELECT artist 
            FROM album WHERE title = ?)''', (album,)
        )
        return self.get_dicts(res)

    def get_artist_by_track(self, track: str) -> List[dict]:
        res = self.cur.execute(
            f'''SELECT * FROM artist WHERE id = (SELECT artist 
            FROM track WHERE title = ?)''', (track,)
        )
        return self.get_dicts(res)

    def get_album_by_track(self, track: str) -> List[dict]:
        res = self.cur.execute(
            f'''SELECT * FROM album WHERE id = (SELECT album
            FROM track WHERE title = ?)''', (track,)
        )
        return self.get_dicts(res)

    def get_genre_by_track(self, track: str) -> List[dict]:
        res = self.cur.execute(
            f'''SELECT * FROM genre WHERE id = (SELECT genre
            FROM track WHERE title = ?)''', (track,)
        )
        return self.get_dicts(res)

    def get_albums_by_artist(self, artist: str) -> List[dict]:
        res = self.cur.execute(
            f'''SELECT * FROM album WHERE artist = (SELECT id
            FROM artist WHERE name = ?)''', (artist,)
        )
        return self.get_dicts(res)

    def get_tracks_by_artist(self, artist: str) -> List[dict]:
        res = self.cur.execute(
            f'''SELECT * FROM track WHERE artist = (SELECT id
            FROM artist WHERE name = ?)''', (artist,)
        )
        return self.get_dicts(res)

    def get_tracks_by_album(self, album: str) -> List[dict]:
        res = self.cur.execute(
            f'''SELECT * FROM track WHERE album = (SELECT id
            FROM album WHERE title = ?)''', (album,)
        )
        return self.get_dicts(res)

    def get_tracks_by_genre(self, genre: str) -> List[dict]:
        res = self.cur.execute(
            f'''SELECT * FROM track WHERE genre = (SELECT id
            FROM genre WHERE name = ?)''', (genre,)
        )
        return self.get_dicts(res)
