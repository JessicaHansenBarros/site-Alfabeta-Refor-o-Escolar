def calcular_salario(lista_alunos):
    print("\n--CALCULAR SALÁRIO--\n")
    print("O usuário tem vale transporte?\n")

    print("1: Sim")
    print("2: Não")
    opção = input("Escolha (1 ou 2): ").strip()

    if opção=="1":
        total = 0
        passe = 0
        for aluno in lista_alunos:
            passe += aluno.data_aula
            total += aluno.valor
        print("\nSeu salário é de:" ,total)
    elif opção=="2":
        total = 0
        for aluno in lista_alunos:
            total += aluno.valor
        print("\nSeu salário é de:" ,total)
    