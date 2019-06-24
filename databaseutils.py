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
    add_index_sql = ''' INSERT OR IGNORE INTO indices(name)
              VALUES(?) '''

    cur = connection.cursor()
    cur.execute(add_index_sql, (index,))

    return cur.lastrowid

def add_tracking(connection, index, data):
    value = data[0]
    time = data[1]

    cur = connection.cursor()

    index_id_sql = ''' SELECT index_id FROM indices WHERE name = ?'''
    index_id = cur.execute(index_id_sql, (index,)).fetchall()[0][0]

    add_tracking_sql = ''' INSERT OR IGNORE INTO tracking(date, value, index_id)
              VALUES(?,?,?) '''

    cur.execute(add_tracking_sql, (time,value,index_id))

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