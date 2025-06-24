import sqlite3
import bcrypt

# Caminho para o nosso ficheiro de banco de dados
DB_PATH = 'biblioteca.db'

def create_user(nome, email, senha_plana, birthdate):
    """
    Cria um novo utilizador no banco de dados.
    Usa bcrypt.hashpw para encriptar a senha.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        hashed_password = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())

        # Insere o novo utilizador na tabela 'usuarios'
        cursor.execute(
            "INSERT INTO usuarios (nome, email, birthdate, senha_hash) VALUES (?, ?, ?, ?)",
            (nome, email, birthdate, hashed_password)
        )
        
        conn.commit()
        return True  # Sucesso

    except sqlite3.IntegrityError:
        print(f"Erro de integridade: O e-mail '{email}' já existe.")
        return False # Falha

    finally:
        if conn:
            conn.close()


def check_login(email, senha_plana):
    
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # Permite aceder aos dados pelo nome da coluna
        cursor = conn.cursor()

        # Primeiro, encontra o utilizador pelo e-mail
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        user_data = cursor.fetchone()

        conn.close() 

        if not user_data:
            return None # Utilizador não encontrado

        hashed_password = user_data['senha_hash']

        # Compara a senha que o utilizador digitou com a senha encriptada
        if bcrypt.checkpw(senha_plana.encode('utf-8'), hashed_password):
            return dict(user_data) # Sucesso, retorna os dados do utilizador
        else:
            return None # Senha incorreta

    except Exception as e:
        print(f"Ocorreu um erro ao verificar o login: {e}")
        return None
        

        
        