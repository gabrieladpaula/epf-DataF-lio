from bottle import request, redirect
import sqlite3
from config import Config

DB_PATH = 'biblioteca.db'

def get_current_user():
    user_email = request.get_cookie("user_email", secret=Config.SECRET_KEY)
    
    if not user_email:
        return None

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (user_email,))
    user = cursor.fetchone()
    conn.close()
    
    return dict(user) if user else None

def admin_required(f):
    def wrapper(*args, **kwargs):
        user = get_current_user()

        if user and user['role'] == 'admin':
            return f(*args, **kwargs)
        else:
            return redirect('/login')
    return wrapper    