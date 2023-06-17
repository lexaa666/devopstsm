from flask import Flask
from flask import Flask
import os
import psycopg2

app = Flask(__name__)
def get_db_connection():
    conn = psycopg2.connect(
        host="database-1.ckbdcqdgeg9o.eu-central-1.rds.amazonaws.com",
        database="foraws",
        user='postgres',
        password='password_1')
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''SELECT date_trunc('day',now());''')
    result = cur.fetchall()
    return f'Lesson42 TSM command postgres now() {result}'



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
