import sqlite3

DB_PATH = 'biblioteca.db'

GENEROS_PARA_ADICIONAR = [
    'Ficção Científica',
    'Fantasia',
    'Romance',
    'Mistério',
    'Thriller',
    'Técnico',
    'História'
]

def popular_generos():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        for nome_genero in GENEROS_PARA_ADICIONAR:
            try:
                cursor.execute("INSERT INTO generos (nome) VALUES (?)", (nome_genero,))
                print(f"Género '{nome_genero}' adicionado com sucesso.")
            except sqlite3.IntegrityError:

                print(f"Género '{nome_genero}' já existe no banco de dados.")

        conn.commit()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    popular_generos()