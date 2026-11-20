from app.models.classes.aula import FabricaAula
from app.models.classes.portal import PortalAlfabeta
from app.models.classes.professor import Professor


def _solicitar_tipo_aula(permitir_vazio: bool = False) -> str | None:
    opcoes = FabricaAula.listar_opcoes()
    codigos_validos = {codigo for codigo, _ in opcoes}
    while True:
        print("\n--SELECIONE O TIPO DE AULA--\n")
        for codigo, descricao in opcoes:
            print(f"{codigo}: {descricao}")
        if permitir_vazio:
            print("Enter: Manter tipo atual")

        opcao = input("Escolha (1, 2, 3, 4 ou 5): ").strip()
        if permitir_vazio and opcao == "":
            return None
        if opcao in codigos_validos:
            return opcao
        print("Opção inválida! Escolha entre 1 e 5.")


def adicionar_aluno(portal: PortalAlfabeta, professor: Professor) -> None:
    nome = input("Nome do aluno: ").strip()
    data_aula = input("Data da aula: ").strip()
    opcao_tipo = _solicitar_tipo_aula()

    try:
        portal.adicionar_aula(
            professor=professor,
            nome_aluno=nome,
            data_aula=data_aula,
            opcao_tipo=opcao_tipo or "1",
        )
        print("--ALUNO ADICIONADO E SALVO COM SUCESSO, RETORNANDO AO MENU--\n")
    except ValueError as erro:
        print(f"Erro ao adicionar aula: {erro}\n")
