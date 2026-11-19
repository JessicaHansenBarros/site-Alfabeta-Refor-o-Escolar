from app.models.classes.portal import PortalAlfabeta
from metodos.login_professor import login_professor
from metodos.registrar_professor import registrar_professor


def menu_inicial(portal: PortalAlfabeta) -> None:
    while True:
        print("\n--MENU--\n")
        print("1: Criar nova conta")
        print("2: Fazer login")
        print("3: Sair")

        opcao = input("Escolha (1, 2 ou 3): ").strip()

        if opcao == "1":
            registrar_professor(portal)
        elif opcao == "2":
            login_professor(portal)
        elif opcao == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Digite (1, 2 ou 3).")
