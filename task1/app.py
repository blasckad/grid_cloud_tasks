from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB_PATH = "/root/db/database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.execute("INSERT INTO users (name) VALUES ('Alice')")
    conn.commit()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)