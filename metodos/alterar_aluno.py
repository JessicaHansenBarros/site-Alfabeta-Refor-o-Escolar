from classes.portal import PortalAlfabeta
from classes.professor import Professor
from metodos.adicionar_aluno import _solicitar_tipo_aula


def alterar_aluno(portal: PortalAlfabeta, professor: Professor) -> None:
    print("\n--- ALTERAR ALUNO / AULA ---")
    aulas = portal.listar_aulas(professor)
    if not aulas:
        print("Nenhuma aula registrada para alterar.")
        return

    for i, aula in enumerate(aulas, start=1):
        print(f"{i}. {aula.descrever()}")

    escolha = input("\nDigite o número do registro para alterar (ou 0 para cancelar): ").strip()
    if escolha == "0":
        print("Alteração cancelada.")
        return

    if not escolha.isdigit():
        print("Entrada inválida!")
        return

    indice = int(escolha) - 1
    if indice < 0 or indice >= len(aulas):
        print("Registro não encontrado!")
        return

    aula_atual = aulas[indice]
    print(f"\nEditando: {aula_atual.descrever()}")
    print("(Deixe em branco e pressione Enter para manter o valor atual.)\n")

    novo_nome = input(f"Novo nome do aluno [{aula_atual.aluno.nome}]: ")
    nova_data = input(f"Nova data da aula [{aula_atual.data_aula}]: ")
    nova_opcao = _solicitar_tipo_aula(permitir_vazio=True)

    try:
        aula_atualizada = portal.alterar_aula(
            professor=professor,
            indice=indice,
            novo_nome_aluno=novo_nome,
            nova_data_aula=nova_data,
            nova_opcao_tipo=nova_opcao,
        )
        print(f"\nRegistro atualizado e salvo: {aula_atualizada.descrever()}")
    except (ValueError, IndexError) as erro:
        print(f"Erro ao alterar registro: {erro}")
