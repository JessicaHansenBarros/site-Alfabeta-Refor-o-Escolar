from classes.professor import Professor
from db.banco_professores import salvar_professores

def registrar_professor(lista_professores):
    print("--REGISTRO DE NOVO PROFESSOR--\n")    
    
    professor_novo = Professor.criar_conta()
    professor_novo.id = len(lista_professores) + 1
    
    lista_professores.append(professor_novo)
    
    lista_professores.sort(key=lambda x:x.nome)

    salvar_professores(lista_professores)
    
    print("Conta criada e salva com sucesso!\n")