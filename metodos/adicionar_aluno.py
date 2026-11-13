from db.banco_alunos import salvar_alunos

from classes.Valores import AlunoMedioIndividual
from classes.Valores import AlunoFimDeSemana
from classes.Valores import AlunoFundamentalColetivo
from classes.Valores import AlunoFundamentalIndividual
from classes.Valores import AlunoMedioColetivo

def adicionar_aluno(lista_alunos, professor = None):
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

    if professor:
        novo_aluno.id_professor = professor.id
    
    lista_alunos.append(novo_aluno)
    lista_alunos.sort(key=lambda x:x.data_aula)

    salvar_alunos(lista_alunos)


    print("--ALUNO ADICIONADO E SALVO COM SUCESSO, RETORNANDO AO MENU--\n")
