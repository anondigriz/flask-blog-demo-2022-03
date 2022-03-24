import sqlite3
from flask import Flask, render_template
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(os.getenv('FLASK_DB'))
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')