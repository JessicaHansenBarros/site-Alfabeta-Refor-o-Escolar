from classes.valores import AlunoMedioIndividual
from classes.valores import AlunoFimDeSemana
from classes.valores import AlunoFundamentalColetivo
from classes.valores import AlunoFundamentalIndividual
from classes.valores import AlunoMedioColetivo

def adicionar_aluno(lista_alunos):
    nome=input("Nome do aluno: ")
    #no proximo projeto adicionar a função do calendário
    data_aula = input("Data da aula: ")


    while True:
        print("\n--SELECIONE O TIPO DE AULA--\n")
        print("1: Fundamental Coletivo")
        print("2: Fundamental Individual")
        print("3: Médio Coletivo")
        print("4: Médio Individual")
        print("5: Fim de Semana")

        opção=input("Escolha (1, 2, 3, 4 ou 5): ").strip()
        if opção=="1":
            novo_aluno = AlunoFundamentalColetivo(nome,data_aula)
            break
        elif opção=="2":
            novo_aluno =AlunoFundamentalIndividual(nome,data_aula)  
            break           
        elif opção=="3":
            novo_aluno =AlunoMedioColetivo(nome,data_aula)
            break
        elif opção=="4":
            novo_aluno =AlunoMedioIndividual(nome,data_aula) 
            break             
        elif opção=="5":
            novo_aluno =AlunoFimDeSemana(nome,data_aula)  
            break
        
    lista_alunos.append(novo_aluno)

    lista_alunos.sort(key=lambda x:x.data_aula)

    print("--ALUNO ADICIONADO COM SUCESSO, RETORNANDO AO MENU--\n")
