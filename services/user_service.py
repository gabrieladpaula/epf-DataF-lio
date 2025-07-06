import sqlite3
import bcrypt

DB_PATH = 'biblioteca.db'

def create_user(nome, email, senha_plana, birthdate):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
        cursor = conn.cursor()
        hashed_password = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
        cursor.execute(
            "INSERT INTO usuarios (nome, email, birthdate, senha_hash) VALUES (?, ?, ?, ?)",
            (nome, email, birthdate, hashed_password)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"Erro de integridade: O e-mail '{email}' já existe.")
        return False
    finally:
        if conn:
            conn.close()

def check_login(email, senha_plana):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        user_data = cursor.fetchone()
        if not user_data:
            return None
        hashed_password = user_data['senha_hash']
        if bcrypt.checkpw(senha_plana.encode('utf-8'), hashed_password):
            return dict(user_data)
        else:
            return None
    except Exception as e:
        print(f"Ocorreu um erro ao verificar o login: {e}")
        return None
    finally:
        if conn:
            conn.close()

def get_all_users():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email, role, birthdate FROM usuarios ORDER BY nome")
        rows = cursor.fetchall()
        users = [dict(row) for row in rows]
        return users
    except Exception as e:
        print(f"Ocorreu um erro ao buscar os usuários: {e}")
        return []
    finally:
        if conn:
            conn.close()
        

        
        