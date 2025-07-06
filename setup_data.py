import sqlite3

DB_PATH = 'biblioteca.db'

livros_para_inserir = [
    {
        "id": 1,
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "sinopse": "Um piloto cai com seu avião no deserto e ali encontra uma criança loura e frágil. Ela diz ter vindo de um pequeno planeta distante. E ali, na convivência com o piloto perdido, os dois repensam os seus valores e encontram o sentido da vida.",
        "caminho_pdf": "https://drive.google.com/file/d/1vucmpK8s0QgdIQKVVKW21gKZesVh2S5j/view?usp=sharing",
        "generos": [5]
    },
    {
        "id": 2,
        "titulo": "O Hobbit",
        "autor": "J. R. R. Tolkien",
        "sinopse": "Acompanha Bilbo Bolseiro, um hobbit pacato que se vê envolvido em uma aventura inesperada. Convidado pelo mago Gandalf e acompanhado por um grupo de anões liderados por Thorin Escudo de Carvalho, Bilbo embarca em uma jornada para recuperar o tesouro e a terra natal dos anões, que foram tomados pelo dragão Smaug. ",
        "caminho_pdf": "https://drive.google.com/file/d/1fdImqKa4TnwjW839dmWq2z6IZNp08Gru/view?usp=sharing",
        "generos": [5]
    },
    {
        "id": 3,
        "titulo": "Dom Quixote",
        "autor": "Miguel de Cervantes",
        "sinopse": "Dom Quixote conta a história de Alonso Quixano, um fidalgo que enlouquece lendo romances de cavalaria e decide se tornar um cavaleiro andante.",
        "caminho_pdf": "https://drive.google.com/file/d/1KzUeem6S2_wIgfw-hGvrIpGO2070zUsJ/view?usp=sharing",
        "generos": [1, 5]
    },
    {
        "id": 4,
        "titulo": "O Alquimista",
        "autor": "Paulo Coelho",
        "sinopse": "A história de Santiago, um jovem pastor andaluz que sonha em encontrar um tesouro escondido nas pirâmides do Egito. Ele embarca em uma jornada de autodescoberta e aprendizado sobre a vida e seus propósitos.",
        "caminho_pdf": "https://drive.google.com/file/d/1vU0v4b5QHYWMq8eY-E9SakwVtYfnpedy/view?usp=sharing",
        "generos": [1]
    },
    {
        "id": 5,
        "titulo": "O céu que nos oprime",
        "autor": "Christine Leunens",
        "sinopse": "Detalhes do livro Integrante da Juventude Hitlerista, ele descobre que seus pais estão escondendo uma jovem judia, Elsa Kor, atrás de uma parede falsa em sua casa, em Viena. Seu horror inicial vira interesse, depois amor e obsessão.",
        "caminho_pdf": "https://drive.google.com/file/d/11F5v_fbjFpVfTeFr89tvodVDgQG1RymU/view?usp=sharing",
        "generos": [2, 6]
    },
    {
        "id": 6,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "sinopse": "Narra a história de Bento Santiago, apelidado de Dom Casmurro, que conta a história de sua vida e de seu amor por Capitu, levantando dúvidas sobre a fidelidade da esposa.",
        "caminho_pdf": "https://drive.google.com/file/d/1Pq0rD0xEdEl9k88lbHKNarMz9yz2XDbv/view?usp=sharing",
        "generos": [5]
    }
]

def popular_banco():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        print("--- INICIANDO SETUP DOS DADOS ---")
        
        print("1. Limpando tabelas 'livros' e 'livros_generos'...")
        cursor.execute("DELETE FROM livros;")
        cursor.execute("DELETE FROM livros_generos;")
        
        print("2. Inserindo dados limpos dos livros...")
        for livro in livros_para_inserir:
            cursor.execute(
                "INSERT INTO livros (id, titulo, autor, sinopse, caminho_pdf) VALUES (?, ?, ?, ?, ?);",
                (livro["id"], livro["titulo"], livro["autor"], livro["sinopse"], livro["caminho_pdf"])
            )
            print(f"   - Livro '{livro['titulo']}' inserido.")

            for genero_id in livro["generos"]:
                cursor.execute(
                    "INSERT INTO livros_generos (livro_id, genero_id) VALUES (?, ?);",
                    (livro["id"], genero_id)
                )
        
        conn.commit()
        print("\n--- SETUP CONCLUÍDO COM SUCESSO! ---")

    except Exception as e:
        print(f"\nOcorreu um erro durante o setup: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    popular_banco()