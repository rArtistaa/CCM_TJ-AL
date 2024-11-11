import sqlite3
import os

def get_connection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '..', 'data', 'database.db')  
    connection = sqlite3.connect(db_path)
    return connection

def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL
                    )''')
    connection.commit()
    cursor.close()
    connection.close()

initialize_database()
