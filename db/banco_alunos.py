import json
import os

CAMINHO_DB_ALUNOS =  os.path.join(os.path.dirname(__file__), "dataBase_alunos.json")

def carregar_alunos():

    # Procura o arquivo, se não houver ou estiver vazio retorna uma lista vazia.
    if not os.path.exists(CAMINHO_DB_ALUNOS) or os.path.getsize(CAMINHO_DB_ALUNOS) == 0:
            return []
    
    try:
        with open(CAMINHO_DB_ALUNOS, "r", encoding = "utf-8") as f:
            return json.load(f)
    
    except json.JSONDecodeError:
        return []


def salvar_alunos(lista_alunos):
     dados_pra_salvar = [aluno.to_dict() for aluno in lista_alunos]

     with open(CAMINHO_DB_ALUNOS, "w", encoding = "utf-8") as f:
          json.dump(dados_pra_salvar, f, indent = 4, ensure_ascii = False)


     
