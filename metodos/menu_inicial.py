from metodos.registrar_professor import registrar_professor
from classes.professor import Professor
from db.banco_professores import carregar_professores


def menu_inicial():
    dados_carregados = carregar_professores()
    lista_professores = [Professor.from_dict(d) for d in dados_carregados]
    while True:
        print("--MENU--\n")
        print("1: Criar nova conta")
        print("2: Fazer login")
        print("3: Sair")

        opção=input("Escolha (1, 2 ou 3):").strip()

        if opção=="1":
            registrar_professor(lista_professores)
        elif opção=="2":
            pass

        elif opção=="3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Digite (1, 2 ou 3)")
