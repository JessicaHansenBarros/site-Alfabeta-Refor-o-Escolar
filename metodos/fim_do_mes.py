from db.banco_alunos import limpar_alunos_do_professor


def limpar_historico(professor):
    while True:
        print("\nDELETAR TODOS OS ALUNOS?\n")
        print("1: Sim")
        print("2: Não")

        opção = input("Escolha (1 ou 2): ").strip()

        if opção == "1":
            limpar_alunos_do_professor(professor.id)
            print("\nHistórico de alunos deletado com sucesso!\n")
            break
        elif opção == "2":
            break
        else:
            print("Opção inválida!")
            