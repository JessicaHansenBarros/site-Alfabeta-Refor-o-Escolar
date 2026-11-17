def exibir_historico(lista_alunos, professor=None):
    print("\n--- HISTÓRICO DE AULAS ---")

    # Se quiser mostrar apenas as aulas do professor logado:
    if professor is not None:
        alunos_exibir = [a for a in lista_alunos if a.id_professor == professor.id]
    else:
        alunos_exibir = lista_alunos

    if not alunos_exibir:
        print("Nenhuma aula registrada até o momento.")
        return

    for i, aluno in enumerate(alunos_exibir, start=1):
        tipo = getattr(aluno, "tipo_de_aula", getattr(aluno, "TipoDeAula", ""))
        print(
            f"{i}. Aluno: {aluno.nome} | "
            f"Data: {aluno.data_aula} | "
            f"Tipo: {tipo} | "
            f"Valor: R$ {aluno.valor:.2f}"
        )

    print(f"\nTotal de aulas registradas: {len(alunos_exibir)}")