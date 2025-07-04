class Livro:
    def __init__(self, id, titulo, autor, sinopse, caminho_pdf):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.sinopse = sinopse
        self.caminho_pdf = caminho_pdf

    def __repr__(self):
        return f"<Livro id={self.id} titulo='{self.titulo}'>"