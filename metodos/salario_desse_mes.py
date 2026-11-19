from classes.portal import PortalAlfabeta
from classes.professor import Professor


def calcular_salario(portal: PortalAlfabeta, professor: Professor) -> None:
    print("\n--CALCULAR SALÁRIO--\n")

    if professor.agenda.esta_vazia():
        print("Nenhuma aula registrada para calcular o salário.")
        return

    print("O usuário tem vale transporte?\n")
    print("1: Sim")
    print("2: Não")
    opcao = input("Escolha (1 ou 2): ").strip()

    if opcao == "1":
        valor_dia = 11.0
        resumo = portal.calcular_salario(professor, valor_vale_diario=valor_dia)


        print(f"\nAulas: R$ {resumo.total_aulas:.2f}")
        print(f"Vale-transporte ({resumo.dias_trabalhados} dia(s)): R$ {resumo.total_vale_transporte:.2f}")
        print(f"Seu salário total é de: R$ {resumo.total_geral:.2f}")
    elif opcao == "2":
        resumo = portal.calcular_salario(professor)
        print(f"\nSeu salário é de: R$ {resumo.total_geral:.2f}")
    else:
        print("Opção inválida!")
