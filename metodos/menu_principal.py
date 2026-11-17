from metodos.adicionar_aluno import adicionar_aluno
from metodos.fim_do_mes import limpar_historico
from metodos.historico_aulas import exibir_historico
from metodos.salario_desse_mes import calcular_salario
from classes.aluno import Aluno
from db.banco_alunos import carregar_alunos

def menu_principal(professor):
    dados_carregados = carregar_alunos()
    lista_alunos = [Aluno.from_dict(d) for d in dados_carregados]
    while True:
        print("\n--MENU PRINCIPAL--\n")
        print("1: Adicionar aluno")
        print("2: Salário desse mês")
        print("3: Alterar aluno")
        print("4: Histórico de aulas")
        print("5: Fim do mês")
        print("6: Deslogar")

        opção=input("Escolha (1, 2, 3, 4 ou 5): ").strip()

        if opção=="1":
            adicionar_aluno(lista_alunos, professor)
        elif opção=="2":
            calcular_salario(lista_alunos, professor)
        elif opção=="3":
            pass
        elif opção=="4":
            exibir_historico(lista_alunos, professor)
        elif opção=="5":
            limpar_historico(lista_alunos)
        elif opção=="6":
            break
        else:
            print("Opção inválida!")
