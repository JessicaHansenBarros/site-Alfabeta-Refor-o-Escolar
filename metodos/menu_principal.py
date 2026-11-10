from metodos.adicionar_aluno import adicionar_aluno

def menu_principal():
    lista_alunos=[]
    while True:
        print("\n--MENU PRINCIPAL--\n")
        print("1: Adicionar aluno")
        print("2: Salário desse mês")
        print("3: Alterar aluno")
        print("4: Histórico de aulas")
        print("5: Fim do mês")

        opção=input("Escolha (1, 2, 3, 4 ou 5): ").strip()

        if opção=="1":
            adicionar_aluno(lista_alunos)
        elif opção=="2":
            pass
        elif opção=="3":
            pass
        elif opção=="4":
            pass
        elif opção=="5":
            pass
        else:
            print("Opção inválida!")
