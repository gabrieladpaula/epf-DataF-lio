from .pessoa import Pessoa

class User(Pessoa):
    def __init__(self, id, nome, email, senha_hash, birthdate=None, role='user'):
        super().__init__(nome, email)

        self.id = id
        self.senha_hash = senha_hash
        self.birthdate = birthdate
        self.role = role

    def __repr__(self):
        return f"<User id={self.id} nome='{self.nome}'>"

    def descrever(self):
        return f"Usuário do sistema: {self.nome}"