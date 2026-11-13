def limpar_historico(lista_alunos):
    while True:
        print("\nDELETAR TODOS OS ALUNOS?\n")
        print("1: Sim")
        print("2: Não")

        opção = input("Escolha (1 ou 2): ").strip()

        if opção =="1":
            lista_alunos.clear()
            print("\nHistórico de alunos deletado com sucesso!\n")
            break
        elif opção=="2":
            break
            