from classes.professor import Professor
from metodos import registrar_professor

lista_professores = []
while True:
    print("--MENU--")
    print("1: Criar nova conta")
    print("2: Fazer login")
    print("3: Sair")

    opção=input("Escolha (1, 2 ou 3):").strip()

    if opção=="1":
        registrar_professor(lista_professores)
    elif opção=="2":
        pass

    elif opção=="3":
        pass
    else:
        print("Opção inválida! Digite (1, 2 ou 3)")




