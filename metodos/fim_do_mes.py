from app.models.classes.portal import PortalAlfabeta
from app.models.classes.professor import Professor


def limpar_historico(portal: PortalAlfabeta, professor: Professor) -> None:
    while True:
        print("\nDELETAR TODOS OS ALUNOS DO SEU HISTÓRICO?\n")
        print("1: Sim")
        print("2: Não")

        opcao = input("Escolha (1 ou 2): ").strip()

        if opcao == "1":
            removidos = portal.finalizar_mes(professor)
            print(f"\nHistórico de alunos deletado e salvo com sucesso! ({removidos} registro(s) removido(s))\n")
            break
        elif opcao == "2":
            break
        else:
            print("Opção inválida! Digite 1 ou 2.")
