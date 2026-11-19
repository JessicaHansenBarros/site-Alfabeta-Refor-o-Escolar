def calcular_salario(lista_alunos, professor=None):
    print("\n--CALCULAR SALÁRIO--\n")

    if professor is not None:
        alunos_prof = [a for a in lista_alunos if a.id_professor == professor.id]
    else:
        alunos_prof = lista_alunos

    if not alunos_prof:
        print("Nenhuma aula registrada para calcular o salário.")
        return

    total_aulas = sum(aluno.valor for aluno in alunos_prof)

    print("O usuário tem vale transporte?\n")
    print("1: Sim")
    print("2: Não")
    opção = input("Escolha (1 ou 2): ").strip()

    if opção == "1":
        valor_dia = 11
        dias_trabalhados = {aluno.data_aula for aluno in alunos_prof}  # set evita contar dias repetidos
        total_passe = len(dias_trabalhados) * valor_dia
        total_final = total_aulas + total_passe

        print(f"\nAulas: R$ {total_aulas:.2f}")
        print(f"Vale-transporte ({len(dias_trabalhados)} dia(s)): R$ {total_passe:.2f}")
        print(f"Seu salário total é de: R$ {total_final:.2f}")

    elif opção == "2":
        print(f"\nSeu salário é de: R$ {total_aulas:.2f}")
    else:
        print("Opção inválida!")