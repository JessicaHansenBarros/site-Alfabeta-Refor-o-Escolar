from classes.portal import PortalAlfabeta
from classes.professor import Professor
from metodos.adicionar_aluno import adicionar_aluno
from metodos.alterar_aluno import alterar_aluno
from metodos.fim_do_mes import limpar_historico
from metodos.historico_aulas import exibir_historico
from metodos.salario_desse_mes import calcular_salario


def menu_principal(portal: PortalAlfabeta, professor: Professor) -> None:
    while True:
        print("\n--MENU PRINCIPAL--\n")
        print("1: Adicionar aluno")
        print("2: Salário desse mês")
        print("3: Alterar aluno")
        print("4: Histórico de aulas")
        print("5: Fim do mês")
        print("6: Deslogar")

        opcao = input("Escolha (1, 2, 3, 4, 5 ou 6): ").strip()

        if opcao == "1":
            adicionar_aluno(portal, professor)
        elif opcao == "2":
            calcular_salario(portal, professor)
        elif opcao == "3":
            alterar_aluno(portal, professor)
        elif opcao == "4":
            exibir_historico(portal, professor)
        elif opcao == "5":
            limpar_historico(portal, professor)
        elif opcao == "6":
            break
        else:
            print("Opção inválida!")
