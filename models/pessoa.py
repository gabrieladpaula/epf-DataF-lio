class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def descrever(self):
        return f"Pessoa: {self.nome}"


