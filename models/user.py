class User:
    def __init__(self, id, nome, email, senha_hash, birthdate=None, role='user'):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash
        self.birthdate = birthdate
        self.role = role  #Permissão de admin

    def __repr__(self):
        return f"<User id={self.id} nome='{self.nome}'>"