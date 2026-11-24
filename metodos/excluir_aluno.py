from app.models.classes.portal import PortalAlfabeta
from app.models.classes.professor import Professor


def excluir_aluno(portal: PortalAlfabeta, professor: Professor) -> None:
    """Remove uma aula específica da agenda do professor logado."""
    print("\n--- EXCLUIR ALUNO / AULA ---")
    aulas = portal.listar_aulas(professor)
    if not aulas:
        print("Nenhuma aula registrada para excluir.")
        return

    for i, aula in enumerate(aulas, start=1):
        print(f"{i}. {aula.descrever()}")

    escolha = input("\nDigite o número do registro para excluir (ou 0 para cancelar): ").strip()
    if escolha == "0":
        print("Exclusão cancelada.")
        return

    if not escolha.isdigit():
        print("Entrada inválida!")
        return

    indice = int(escolha) - 1
    if indice < 0 or indice >= len(aulas):
        print("Registro não encontrado!")
        return

    aula_selecionada = aulas[indice]
    print(f"\nSelecionado: {aula_selecionada.descrever()}")
    confirmacao = input("Confirmar exclusão? (1: Sim | 2: Não): ").strip()
    if confirmacao != "1":
        print("Exclusão cancelada.")
        return

    try:
        aula_removida = portal.remover_aula(professor, indice)
        print(f"\nRegistro excluído e salvo com sucesso: {aula_removida.descrever()}")
    except (ValueError, IndexError) as erro:
        print(f"Erro ao excluir registro: {erro}")
