import sqlite3
from typing import Optional

DB_PATH = 'filemeta.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password_hash TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS files (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT,
                    stored_name TEXT,
                    uploader TEXT,
                    size INTEGER,
                    created_at TEXT
                )''')
    conn.commit()
    conn.close()

def add_user(username: str, pw_hash: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, pw_hash))
    conn.commit()
    conn.close()

def get_user(username: str) -> Optional[tuple]:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, username, password_hash FROM users WHERE username=?", (username,))
    res = c.fetchone()
    conn.close()
    return res

def add_file(filename: str, stored_name: str, uploader: str, size: int, created_at: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO files (filename, stored_name, uploader, size, created_at) VALUES (?, ?, ?, ?, ?)",
              (filename, stored_name, uploader, size, created_at))
    conn.commit()
    conn.close()

def list_files():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, filename, stored_name, uploader, size, created_at FROM files")
    res = c.fetchall()
    conn.close()
    return res

def get_file(stored_name: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, filename, stored_name, uploader, size, created_at FROM files WHERE stored_name=?", (stored_name,))
    res = c.fetchone()
    conn.close()
    return res
