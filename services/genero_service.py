import sqlite3

DB_PATH = 'biblioteca.db'

def create_genre(nome):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO generos (nome) VALUES (?)", (nome,))

        conn.commit()
        print(f"Género '{nome}' criado com sucesso.")
        return True

    except sqlite3.IntegrityError:
        # Este erro acontece se o nome do género já existir 
        print(f"Erro: O género '{nome}' já existe.")
        return False

    finally:
        if conn:
            conn.close()


def get_all_genres():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM generos ORDER BY nome")
        rows = cursor.fetchall()

        # Converte as linhas em uma lista de dicionários
        genres = [dict(row) for row in rows]

        return genres

    except Exception as e:
        print(f"Ocorreu um erro ao buscar os géneros: {e}")
        return []

    finally:
        if conn:
            conn.close()

