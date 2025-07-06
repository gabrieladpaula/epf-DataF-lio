import sqlite3

DB_PATH = 'biblioteca.db'
LIVRO_ID_TESTE = 999  # Usamos um ID alto para não conflitar

# Texto de teste com muitos acentos
titulo_teste = "Teste de Inserção com Acentuação e Çedilha"
autor_teste = "José de Alencar"
sinopse_teste = "Verificando se a comunicação com o SQLite está em UTF-8."
caminho_teste = "/static/pdfs/teste.pdf"

print("--- INICIANDO TESTE DE ENCODING NO BANCO DE DADOS ---")

try:
    # Conecta ao banco
    conn = sqlite3.connect(DB_PATH)
    # ESTA LINHA É CRUCIAL
    conn.text_factory = str
    cursor = conn.cursor()

    # Garante que não há lixo de testes anteriores
    cursor.execute("DELETE FROM livros WHERE id = ?", (LIVRO_ID_TESTE,))
    conn.commit()
    print("1. Limpeza de teste antigo concluída.")

    # Insere o novo livro de teste
    cursor.execute(
        "INSERT INTO livros (id, titulo, autor, sinopse, caminho_pdf) VALUES (?, ?, ?, ?, ?)",
        (LIVRO_ID_TESTE, titulo_teste, autor_teste, sinopse_teste, caminho_teste)
    )
    conn.commit()
    print("2. Novo livro de teste com acentos INSERIDO com sucesso.")

    # Agora, lê imediatamente o que acabamos de inserir
    cursor.execute("SELECT titulo, autor, sinopse FROM livros WHERE id = ?", (LIVRO_ID_TESTE,))
    livro_lido = cursor.fetchone()
    print("3. Leitura do livro de teste CONCLUÍDA.")

    # Limpa o livro de teste do banco
    cursor.execute("DELETE FROM livros WHERE id = ?", (LIVRO_ID_TESTE,))
    conn.commit()

    print("\n--- RESULTADO DO TESTE ---")
    if livro_lido:
        print("Título Lido: ", livro_lido[0])
        print("Autor Lido:  ", livro_lido[1])
        print("Sinopse Lido:", livro_lido[2])
    else:
        print("ERRO: Não foi possível ler o livro de teste.")

except Exception as e:
    print(f"\nOcorreu um erro durante o teste: {e}")

finally:
    if conn:
        conn.close()
    print("\n--- TESTE FINALIZADO ---")