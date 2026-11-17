from metodos.registrar_professor import registrar_professor
from metodos.login_professor import login_professor


def menu_inicial():
    while True:
        print("\n--MENU--\n")
        print("1: Criar nova conta")
        print("2: Fazer login")
        print("3: Sair")

        opção = input("Escolha (1, 2 ou 3): ").strip()

        if opção == "1":
            registrar_professor()
        elif opção == "2":
            login_professor()
        elif opção == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Digite (1, 2 ou 3)")
