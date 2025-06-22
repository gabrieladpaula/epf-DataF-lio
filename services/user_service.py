import sqlite3
import bcrypt

#Caminho do banco de dados
DB_PATH = 'biblioteca.db'

def create_user(nome, email, senha_plana, birthdate):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        hashed_pass = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())

        cursor.execute(
            'INSERT INTO usuarios (nome, email, senha_hash, birthdata) VALUES (?, ?, ?, ?)',
            (nome, email, hashed_pass, birthdate)
        )

        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(F"Erro de integridade: o email '{email}' já cadastrado.")
        return False
    finally:
        if conn:
            conn.close()
        