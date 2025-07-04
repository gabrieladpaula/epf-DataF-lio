import sqlite3

DB_PATH = 'biblioteca.db'

def create_book(titulo, autor, sinopse, caminho_pdf):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO livros (titulo, autor, sinopse, caminho_pdf) VALUES (?, ?, ?, ?)",
            (titulo, autor, sinopse, caminho_pdf)
        )

        # Obter o ID do livro criado
        novo_livro_id = cursor.lastrowid

        conn.commit()
        print(f"Livro '{titulo}' criado com sucesso com o ID: {novo_livro_id}")
        return novo_livro_id

    except sqlite3.IntegrityError as e:
        # Este erro acontece se o caminho_pdf já existir (porque definimos a coluna como UNIQUE)
        print(f"Erro de integridade ao criar o livro: {e}")
        return None

    finally:
        if conn:
            conn.close()

def get_all_books():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM livros")
        rows = cursor.fetchall()

        books = [dict(row) for row in rows]
        return books
    
    except sqlite3.Error as e:
        print(f"Erro ao buscar livros: {e}")
        return []
    finally:
        if conn:
            conn.close()    

# ... o teu código da função create_book está aqui em cima ...


def get_all_books():
    """
    Busca todos os livros da tabela 'livros'.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row # Permite aceder aos dados por nome da coluna
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM livros")
        rows = cursor.fetchall()

        # Converte as linhas do banco de dados em uma lista de dicionários
        books = [dict(row) for row in rows]

        return books

    except Exception as e:
        print(f"Ocorreu um erro ao buscar os livros: {e}")
        return [] # Retorna uma lista vazia em caso de erro

    finally:
        if conn:
            conn.close()


def get_book_by_id(livro_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
        row = cursor.fetchone()

        return dict(row) if row else None

    except Exception as e:
        print(f"Erro ao buscar o livro: {e}")
        return None

    finally:
        if conn:
            conn.close()


def update_book(livro_id, titulo, autor, sinopse):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE livros SET titulo = ?, autor = ?, sinopse = ? WHERE id = ?",
            (titulo, autor, sinopse, livro_id)
        )

        conn.commit()
        print(f"Livro com ID {livro_id} atualizado com sucesso.")
        return True

    except Exception as e:
        print(f"Erro ao atualizar o livro: {e}")
        return False

    finally:
        if conn:
            conn.close()


def delete_book(livro_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))

        conn.commit()
        print(f"Livro com ID {livro_id} apagado com sucesso.")
        return True

    except Exception as e:
        print(f"Erro ao apagar o livro: {e}")
        return False

    finally:
        if conn:
            conn.close()
        