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
        novo_livro_id = cursor.lastrowid
        conn.commit()
        return novo_livro_id
    except sqlite3.IntegrityError as e:
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
    except Exception as e:
        print(f"Ocorreu um erro ao buscar os livros: {e}")
        return []
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
        print(f"Ocorreu um erro ao buscar o livro: {e}")
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
        return True
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o livro: {e}")
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
        return True
    except Exception as e:
        print(f"Ocorreu um erro ao apagar o livro: {e}")
        return False
    finally:
        if conn:
            conn.close()
        