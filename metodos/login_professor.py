from app.models.classes.portal import PortalAlfabeta
from app.models.classes.professor import Professor
from metodos.menu_principal import menu_principal


def login_professor(portal: PortalAlfabeta) -> Professor | None:
    print("\n--- LOGIN DO PROFESSOR ---")

    if not portal.professores:
        print("Nenhum professor cadastrado ainda! Crie uma conta primeiro.")
        return None

    login_digitado = input("Login: ").strip()
    senha_digitada = input("Senha: ").strip()

    professor = portal.autenticar(login_digitado, senha_digitada)
    if professor is not None:
        print(f"\nBem-vindo(a), {professor.nome}!")
        print(professor.exibir_identificacao())
        menu_principal(portal, professor)
        return professor

    print("\nErro: Login ou senha incorretos!")
    return None
