from dataclasses import dataclass
@dataclass

class professor:
    def __init__(self, nome, email, login, senha):
        self.nome = nome
        self.email = email
        self.login = login
        self.senha = senha
    