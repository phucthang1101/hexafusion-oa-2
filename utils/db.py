import sqlite3
from datetime import datetime

conn = sqlite3.connect("logs.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS ai_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    input TEXT,
    output TEXT
)
""")
conn.commit()

def insert_log(input_text, output_text):
    cur.execute(
        "INSERT INTO ai_logs (timestamp, input, output) VALUES (?, ?, ?)",
        (datetime.utcnow().isoformat(), input_text, output_text)
    )
    conn.commit()

def get_latest_logs(n=10):
    cur.execute("SELECT timestamp, input, output FROM ai_logs ORDER BY id DESC LIMIT ?", (n,))
    return cur.fetchall()
