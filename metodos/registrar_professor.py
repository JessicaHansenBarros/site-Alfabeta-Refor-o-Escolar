from classes.professor import Professor

def registrar_professor(lista_professores):
    print("--REGISTRO DE NOVO PROFESSOR--")    
    professor_logado=Professor.criar_conta()
    lista_professores.append(professor_logado)
    lista_professores.sort(key=lambda x:x.nome)
    print("Conta criada com sucesso")