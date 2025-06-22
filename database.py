import sqlite3

DB_NAME = 'biblioteca.db'

def criar_tabelas():
    """Cria as tabelas no banco de dados se elas não existirem."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Tabela de utilizadores
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        birthdata TEXT,           
        senha_hash TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'user'
    );
    ''')

    # Tabela de livros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        sinopse TEXT,
        caminho_pdf TEXT NOT NULL UNIQUE
    );
    ''')

    # Tabela de generos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS generos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
    );
    ''')

    # Tabela de ligação livros <-> géneros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros_generos (
        livro_id INTEGER,
        genero_id INTEGER,
        FOREIGN KEY (livro_id) REFERENCES livros(id) ON DELETE CASCADE,
        FOREIGN KEY (genero_id) REFERENCES generos(id) ON DELETE CASCADE,
        PRIMARY KEY (livro_id, genero_id)
    );
    ''')

    # Tabela de histórico de downloads
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS historico_downloads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        livro_id INTEGER,
        data_download TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
        FOREIGN KEY (livro_id) REFERENCES livros(id) ON DELETE CASCADE
    );
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados e tabelas criados com sucesso!")

if __name__ == '__main__':
    criar_tabelas()