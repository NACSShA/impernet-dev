import sqlite3
from config import DB_NAME


def get_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        telegram_id INTEGER PRIMARY KEY,
        login TEXT,
        login_lower TEXT UNIQUE,
        access_level TEXT DEFAULT 'guest',
        description TEXT DEFAULT '',
        profile_private INTEGER DEFAULT 0,
        registration_state TEXT DEFAULT 'none',
        warnings INTEGER DEFAULT 0,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()
