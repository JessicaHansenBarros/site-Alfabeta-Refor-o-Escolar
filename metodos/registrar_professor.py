from classes.portal import PortalAlfabeta
from classes.professor import Professor


def registrar_professor(portal: PortalAlfabeta) -> Professor | None:
    print("\n--- CADASTRO DE NOVO PROFESSOR ---")
    nome = input("Nome completo: ")
    email = input("Email: ")
    login = input("Login: ")
    senha = input("Senha: ")

    try:
        professor = portal.registrar_professor(
            nome=nome,
            email=email,
            login=login,
            senha=senha,
        )
        print("Conta criada e salva com sucesso! Retornando ao menu de login.\n")
        return professor
    except ValueError as erro:
        print(f"Erro ao cadastrar professor: {erro}\n")
        return None
