from dataclasses import dataclass
@dataclass

class Professor:
    def __init__(self, nome, email, login, senha):
        self.nome = nome
        self.email = email
        self.login = login
        self.senha = senha

    @staticmethod
    def criar_conta():
        print("\n--- CADASTRO DE NOVO PROFESSORES ---")
        nome = input("Nome completo: ")
        email = input("Email: ")
        login = input("Login: ")
        senha = input("Senha: ")
        print("Usuário cadastrado com sucesso! Retornando ao menu de login.")
        return Professor(nome, email, login, senha)   
    