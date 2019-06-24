import sqlite3

sql_create_tables = [""" CREATE TABLE IF NOT EXISTS indices (
                         index_id INTEGER PRIMARY KEY,
                         name     TEXT NOT NULL,
                        UNIQUE(name)
                     ); """,
                     """ CREATE TABLE IF NOT EXISTS tracking (
                         track_id INTEGER PRIMARY KEY,
                         date     TEXT NOT NULL,
                         value    INTEGER NOT NULL,
                         index_id INTEGER,
                         FOREIGN KEY(index_id) REFERENCES indices(id),
                         UNIQUE(date, index_id)
                     ); """]

def add_index(connection, index):
    sql = ''' INSERT OR IGNORE INTO indices(name)
              VALUES(?) '''

    cur = connection.cursor()
    cur.execute(sql, (index,))

    return cur.lastrowid

def create_tables(connection):
    try:
        c = connection.cursor()
        for sql in sql_create_tables:
            c.execute(sql)
    except sqlite3.Error as e:
        print(e)

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)

    return None