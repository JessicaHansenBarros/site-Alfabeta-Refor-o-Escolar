from dataclasses import dataclass
@dataclass

class Professor:
    def __init__(self, nome, email, login, senha, id = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.login = login
        self.senha = senha

    # Essa função converte os dados do professor pra dicionário pra facilitar na escrita no json.
    def to_dict(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "email" : self.email,
            "login" : self.login,
            "senha" : self.senha
        }


    @classmethod
    def from_dict(cls, dados: dict):
        # Reconstrói um objeto Professor a partir dos dados fornecidos pelo JSON
        return cls(
            nome = dados["nome"],
            email = dados["email"],
            login = dados["login"],
            senha = dados["senha"],
            id = dados.get("id")
        )

    @staticmethod
    def criar_conta():
        print("\n--- CADASTRO DE NOVO PROFESSORES ---")
        nome = input("Nome completo: ")
        email = input("Email: ")
        login = input("Login: ")
        senha = input("Senha: ")
        print("Usuário cadastrado com sucesso! Retornando ao menu de login.")
        return Professor(nome, email, login, senha)   
    