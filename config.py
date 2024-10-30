import sqlite3


def get_connection():
    connection = sqlite3.connect('database.db')
    return connection


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                    )''')
    connection.commit()
    cursor.close()
    connection.close()

initialize_database()