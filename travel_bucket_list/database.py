import sqlite3


DATABASE_NAME = "travel.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS destinations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT NOT NULL,
            city TEXT NOT NULL,
            budget REAL DEFAULT 0,
            priority TEXT DEFAULT 'Medium',
            status TEXT DEFAULT 'Wishlist',
            travel_date TEXT,
            notes TEXT,
            capital TEXT,
            region TEXT,
            currency TEXT,
            flag TEXT
        )
    """)

    connection.commit()

    connection.close()