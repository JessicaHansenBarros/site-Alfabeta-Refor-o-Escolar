import json
import os

CAMINHO_DB =  os.path.join(os.path.dirname(__file__), "dataBase_professor.json")

# Carrega os professores da lista JSON
def carregar_professores():

    # Procura o arquivo, se não houver ou estiver vazio retorna uma lista vazia.
    if not os.path.exists(CAMINHO_DB) or os.path.getsize(CAMINHO_DB) == 0:
        return []

    try:
        with open(CAMINHO_DB, "r", encoding = "utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError:
        return []


# Converte a lista de professores pra dict e salva no arquivo JSON
def salvar_professores(lista_professores):
    dados_pra_salvar = [prof.to_dict() for prof in lista_professores]

    with open(CAMINHO_DB, "w", encoding = "utf-8") as f:
        # indent=4 formata e deixa o JSON legível.
        # ensure_ascii=False preserva os acentos(ex: 'Cauã', 'Matemática')
        json.dump(dados_pra_salvar, f, indent=4, ensure_ascii = False)