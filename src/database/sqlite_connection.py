import sqlite3

db = sqlite3.connect('dev-database.db')

def create_table():
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE order(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    status INTEGER NOT NULL,
    price INTEGER NOT NULL,
    user_id INTEGER NOT NULL,)''')

