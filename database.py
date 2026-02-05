import sqlite3
from datetime import datetime

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    telegram_id INTEGER PRIMARY KEY,
    marzban_username TEXT,
    expire_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS payments (
    invoice_id TEXT PRIMARY KEY,
    telegram_id INTEGER,
    tariff TEXT,
    status TEXT
)
""")

conn.commit()


def get_user(telegram_id: int):
    cursor.execute("SELECT * FROM users WHERE telegram_id=?", (telegram_id,))
    return cursor.fetchone()


def save_user(telegram_id, username, expire_at):
    cursor.execute(
        "INSERT OR REPLACE INTO users VALUES (?, ?, ?)",
        (telegram_id, username, expire_at)
    )
    conn.commit()


def save_payment(invoice_id, telegram_id, tariff):
    cursor.execute(
        "INSERT INTO payments VALUES (?, ?, ?, 'pending')",
        (invoice_id, telegram_id, tariff)
    )
    conn.commit()


def mark_payment_paid(invoice_id):
    cursor.execute(
        "UPDATE payments SET status='paid' WHERE invoice_id=?",
        (invoice_id,)
    )
    conn.commit()


def get_payment(invoice_id):
    cursor.execute(
        "SELECT * FROM payments WHERE invoice_id=?",
        (invoice_id,)
    )
    return cursor.fetchone()
