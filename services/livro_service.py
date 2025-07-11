import sqlite3

DB_PATH = 'biblioteca.db'

def create_book(titulo, autor, sinopse, caminho_pdf):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
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
        conn.text_factory = str
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        rows = cursor.fetchall()
        books = [dict(row) for row in rows]
        for book in books:
            for key, value in book.items():
                if isinstance(value, bytes):
                    book[key] = value.decode('latin-1')
        return books
    except Exception as e:
        print(f"Ocorreu um erro ao buscar os livros: {e}")
        return []
    finally:
        if conn:
            conn.close()

def get_all_generos():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM generos")
        return [dict(row) for row in cursor.fetchall()]
    finally:
        if conn:
            conn.close()

def get_book_by_id(livro_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
        row = cursor.fetchone()
        if not row:
            return None
        book = dict(row)
        for key, value in book.items():
            if isinstance(value, bytes):
                book[key] = value.decode('latin-1')
        return book
    except Exception as e:
        print(f"Ocorreu um erro ao buscar o livro: {e}")
        return None
    finally:
        if conn:
            conn.close()

def update_book(livro_id, titulo, autor, sinopse, caminho_pdf):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE livros SET titulo = ?, autor = ?, sinopse = ?, caminho_pdf = ? WHERE id = ?",
            (titulo, autor, sinopse, caminho_pdf, livro_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o livro: {e}")
        return False
    finally:
        if conn:
            conn.close()

def update_livro_generos(livro_id, novos_generos_ids):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros_generos WHERE livro_id = ?", (livro_id,))
        for genero_id in novos_generos_ids:
            cursor.execute(
                "INSERT INTO livros_generos (livro_id, genero_id) VALUES (?, ?)",
                (livro_id, int(genero_id))
            )
        conn.commit()
        return True
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar os géneros do livro: {e}")
        return False
    finally:
        if conn:
            conn.close()

def get_genres_por_book(livro_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
        cursor = conn.cursor()
        cursor.execute("SELECT genero_id FROM livros_generos WHERE livro_id = ?", (livro_id,))
        return [row[0] for row in cursor.fetchall()]
    finally:
        if conn:
            conn.close()

def delete_book(livro_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
        cursor.execute("DELETE FROM livros_generos WHERE livro_id = ?", (livro_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Ocorreu um erro ao apagar o livro: {e}")
        return False
    finally:
        if conn:
            conn.close()

def link_book_to_genres(livro_id, generos_ids):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
        cursor = conn.cursor()
        for genero_id in generos_ids:
            cursor.execute(
                "INSERT INTO livros_generos (livro_id, genero_id) VALUES (?, ?)",
                (livro_id, int(genero_id))
            )
        conn.commit()
        return True
    except Exception as e:
        print(f"Ocorreu um erro ao ligar o livro aos géneros: {e}")
        return False
    finally:
        if conn:
            conn.close()

def search_books(query):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.text_factory = str
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        search_term = f"%{query}%"
        cursor.execute(
            "SELECT * FROM livros WHERE titulo LIKE ? OR autor LIKE ?",
            (search_term, search_term)
        )
        rows = cursor.fetchall()
        books = [dict(row) for row in rows]
        for book in books:
            for key, value in book.items():
                if isinstance(value, bytes):
                    book[key] = value.decode('latin-1')
        return books
    except Exception as e:
        print(f"Ocorreu um erro ao buscar os livros: {e}")
        return []
    finally:
        if conn:
            conn.close()          
        